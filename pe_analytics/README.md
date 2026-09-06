# pe_analytics

Forensic diligence and valuation tooling for private equity — built to match
the course modules, and built to be honest about what machines can and cannot do.

```bash
python3 -m pe_analytics.run_demo
```

Runs end-to-end on synthetic data with issues deliberately planted, so you can
verify the detectors actually catch things.

---

## What's automatable, and what isn't

| Task | Automatable | Why |
|---|---|---|
| Proof of cash (revenue → bank deposits) | **Fully** | Deterministic reconciliation over thousands of rows |
| Anomaly detection (round numbers, period-end spikes, Benford) | **Yes** | Statistical pattern-finding at scale |
| Flagging *candidate* add-backs, serial "one-offs" | **Yes** | "Appeared in 4 of 5 years" is a query, not a judgment |
| Document extraction from contracts/GL exports | **Yes (LLMs)** | Text → structure |
| **Deciding if an add-back is legitimate** | **No** | Needs a forward-looking view of *this* business |
| Setting the NWC peg | **Partly** | T12M average is trivial; "normal" needs context |
| Customer concentration, management quality | **No** | Judgment |

The pattern: **AI removes the clerical 80% and surfaces exceptions; the 20%
that moves the price is still judgment.** That's the difference between
sampling 5% of transactions and testing 100% — real value, but not a
replacement for the deal team.

## Why not TensorFlow

Deep learning wins on large, high-dimensional, homogeneous data. PE analytics
is the opposite: **small-n, tabular, heterogeneous, sparse.** You have 8–15
comparables, not 8 million. A neural net on 12 comps memorizes the table and
predicts nothing.

On tabular data at this scale, gradient boosting and plain regression
consistently beat neural nets — and regression is *interpretable*, which
matters when you must defend a number across a negotiating table. Uses
numpy / pandas / scikit-learn only.

**DCF isn't a prediction problem at all.** It's a deterministic calculation.
ML can forecast the *inputs*, but terminal value is ~70% of the answer and no
model improves a guess about year-6-to-infinity. What helps is Monte Carlo:
report a distribution instead of false precision.

---

## Modules

### `qoe_forensics` — the automatable part of Quality of Earnings
- `proof_of_cash` — ties recognized revenue to bank deposits; flags a
  **widening** gap (a stable gap is just collection lag)
- `period_end_cutoff` — revenue concentration in the last days of a quarter
  vs. uniform expectation; catches channel stuffing
- `serial_addbacks` — the highest-value automated check: which "one-offs"
  recur, and which are forward-looking pro-forma claims
- `benford_first_digit` — leading-digit screen with Nigrini MAD thresholds
- `round_number_bias` — clusters of round manual entries

Every detector returns a `Finding` (severity + headline + detail table) —
**exceptions for a human, never verdicts.**

### `comps` — extrinsic valuation
Median peer multiple *plus* a regression of EV/EBITDA on growth and margin, so
you predict the multiple the target's own fundamentals justify rather than
applying a peer average. Reports R², warns when extrapolating outside the peer
envelope, and returns a **range**, because with n=12 a point estimate is fiction.

### `dcf` — intrinsic valuation
Driver-based FCF projection (note: NWC scales with revenue *growth*, encoding
the "growth eats cash" lesson), perpetuity or exit-multiple terminal value,
plus:
- `tornado` — one-at-a-time sensitivity: which assumption actually drives it
- `monte_carlo` — 10k sims across the fragile inputs → a distribution

### `forecast` — driver forecasting, scored honestly
- **Walk-forward validation** (expanding window, no shuffling) — random splits
  leak the future and produce accuracy that evaporates in production
- **Baseline comparison** against naive-last-value and linear-trend. If the
  model loses, `verdict()` says so plainly. In the demo it *does* lose to a
  trend line — which is the correct, useful finding.

---

## Extending it

Swap synthetic data for real data by passing your own DataFrames:

```python
from pe_analytics import qoe_forensics, comps, dcf

txns    = pd.read_csv("gl_export.csv", parse_dates=["date"])   # date, amount
monthly = pd.read_csv("monthly.csv")   # month, revenue_recognized, cash_deposits
addbacks= pd.read_csv("addbacks.csv")  # item, FY2021..FY2025

for f in qoe_forensics.run_all(txns, monthly, addbacks):
    print(f)
```

Natural next additions:
- **Customer-level cohort/retention analysis** (churn, net revenue retention) —
  high diligence value, genuinely quantitative
- **Related-party & duplicate-payment detection** (fuzzy vendor matching)
- **NWC seasonality decomposition** to set a defensible peg from monthly data
- **LBO engine** (sources & uses, debt schedule, returns) — Module 4/5

## Caveats worth repeating

- Benford is a **screen**, not evidence. Legitimate data fails it for boring
  structural reasons (price points, contractual amounts, narrow ranges).
- Recursive multi-step forecasts **compound error** — trust period 1, not period 4.
- Synthetic demo data proves the code runs; it proves nothing about real accuracy.
- Every flag needs a human to ask *why*. The tool narrows where to look.
