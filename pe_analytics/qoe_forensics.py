"""
qoe_forensics — the automatable part of Quality of Earnings.

Every function here returns EXCEPTIONS FOR A HUMAN, never a conclusion.
The distinction matters: `serial_addbacks` can tell you a restructuring charge
appeared in 4 of 5 years, which is a fact about the data. It cannot tell you
whether restructuring will recur next year, which is what actually determines
whether the add-back is legitimate. That judgment stays with the deal team.

Detectors
---------
proof_of_cash      does recognized revenue actually show up in the bank?
benford_first_digit are the leading digits distributed as real financial data is?
period_end_cutoff  are sales being pulled forward into the measurement period?
round_number_bias  are there implausible clusters of round manual entries?
serial_addbacks    is a "one-off" appearing every single year?
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

# Expected first-digit frequencies under Benford's law
BENFORD = np.log10(1 + 1 / np.arange(1, 10))


@dataclass
class Finding:
    """A single exception raised for human review."""

    check: str
    severity: str  # "high" | "medium" | "low" | "clear"
    headline: str
    detail: pd.DataFrame | None = field(default=None, repr=False)

    def __str__(self) -> str:
        mark = {"high": "[HIGH]", "medium": "[MED ]", "low": "[LOW ]", "clear": "[ ok ]"}[self.severity]
        return f"{mark} {self.check}: {self.headline}"


# ----------------------------------------------------------------------------
# 1. Proof of cash — the signature QoE technique
# ----------------------------------------------------------------------------
def proof_of_cash(
    monthly: pd.DataFrame,
    revenue_col: str = "revenue_recognized",
    cash_col: str = "cash_deposits",
    period_col: str = "month",
    tolerance: float = 0.05,
) -> Finding:
    """Tie recognized revenue to cash deposits.

    Revenue can be manufactured on paper; bank deposits are far harder to fake.
    A persistent and WIDENING gap is the signal — a stable gap is usually just
    normal collection lag, while a widening one suggests revenue is being
    recognized that never converts to cash.
    """
    df = monthly.copy()
    df["gap"] = df[revenue_col] - df[cash_col]
    df["gap_pct"] = df["gap"] / df[revenue_col]

    # Is the gap trending wider over time? (slope of gap_pct vs time index)
    x = np.arange(len(df))
    slope = np.polyfit(x, df["gap_pct"].to_numpy(), 1)[0] if len(df) > 2 else 0.0
    annualized_drift = slope * 12

    breaches = df[df["gap_pct"] > tolerance]
    recent = df["gap_pct"].tail(6).mean()

    if annualized_drift > 0.02 and recent > tolerance:
        sev = "high"
        head = (
            f"collection gap widening ~{annualized_drift*100:.1f}pp/yr; "
            f"last-6-month average gap {recent*100:.1f}% of revenue"
        )
    elif len(breaches) > len(df) * 0.25:
        sev = "medium"
        head = f"{len(breaches)}/{len(df)} months exceed the {tolerance*100:.0f}% tolerance"
    else:
        sev = "clear"
        head = f"revenue ties to cash within tolerance (avg gap {df['gap_pct'].mean()*100:.1f}%)"

    detail = df[[period_col, revenue_col, cash_col, "gap", "gap_pct"]]
    return Finding("proof_of_cash", sev, head, detail)


# ----------------------------------------------------------------------------
# 2. Benford's law
# ----------------------------------------------------------------------------
def benford_first_digit(amounts: pd.Series | np.ndarray) -> Finding:
    """Compare leading-digit frequencies to Benford's law.

    Honest caveat: Benford is a SCREEN, not evidence. Legitimate datasets fail
    it for boring structural reasons (price points, contractual amounts,
    tight ranges). Treat a failure as "look here", never as "fraud".
    """
    a = pd.Series(amounts).abs()
    a = a[a > 0]
    lead = a.astype(str).str.replace(r"[^1-9]", "", regex=True).str[:1]
    lead = pd.to_numeric(lead[lead != ""], errors="coerce").dropna().astype(int)

    observed = np.array([(lead == d).sum() for d in range(1, 10)], dtype=float)
    n = observed.sum()
    if n < 300:
        return Finding("benford", "low", f"only {int(n)} usable amounts — sample too small to screen")

    expected = BENFORD * n
    chi2 = float(((observed - expected) ** 2 / expected).sum())
    mad = float(np.abs(observed / n - BENFORD).mean())

    # Nigrini's conventional MAD thresholds for first-digit tests
    if mad < 0.006:
        sev, verdict = "clear", "close conformity"
    elif mad < 0.012:
        sev, verdict = "low", "acceptable conformity"
    elif mad < 0.015:
        sev, verdict = "medium", "marginal conformity"
    else:
        sev, verdict = "high", "nonconformity"

    detail = pd.DataFrame(
        {
            "digit": range(1, 10),
            "observed_pct": observed / n,
            "expected_pct": BENFORD,
            "difference": observed / n - BENFORD,
        }
    )
    return Finding("benford", sev, f"{verdict} (MAD={mad:.4f}, chi2={chi2:.1f})", detail)


# ----------------------------------------------------------------------------
# 3. Period-end cutoff testing (channel stuffing)
# ----------------------------------------------------------------------------
def period_end_cutoff(
    txns: pd.DataFrame,
    date_col: str = "date",
    amount_col: str = "amount",
    window_days: int = 3,
) -> Finding:
    """Detect revenue pulled forward into the last days of a quarter.

    Compares the share of revenue booked in the final `window_days` of each
    quarter against the share you'd expect if sales landed uniformly. A ratio
    meaningfully above 1.0 means business is clustering at the deadline —
    the classic 'borrowing from next quarter' pattern.
    """
    df = txns.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df["quarter"] = df[date_col].dt.to_period("Q")
    df["q_end"] = df["quarter"].dt.end_time.dt.normalize()
    df["days_to_q_end"] = (df["q_end"] - df[date_col].dt.normalize()).dt.days
    df["in_window"] = df["days_to_q_end"] < window_days

    rows = []
    for q, g in df.groupby("quarter"):
        q_days = (g["q_end"].iloc[0] - q.start_time.normalize()).days + 1
        expected_share = window_days / q_days
        actual_share = g.loc[g["in_window"], amount_col].sum() / g[amount_col].sum()
        rows.append(
            {
                "quarter": str(q),
                "expected_share": expected_share,
                "actual_share": actual_share,
                "concentration_ratio": actual_share / expected_share,
            }
        )
    out = pd.DataFrame(rows)

    worst = out["concentration_ratio"].max()
    recent = out["concentration_ratio"].tail(4).mean()
    trend_up = out["concentration_ratio"].tail(4).mean() > out["concentration_ratio"].head(4).mean() * 1.3

    if recent > 2.0 and trend_up:
        sev = "high"
        head = (
            f"quarter-end revenue concentration {recent:.1f}x expected in the last year "
            f"and worsening — classic pull-forward / channel-stuffing pattern"
        )
    elif worst > 2.0:
        sev = "medium"
        head = f"at least one quarter shows {worst:.1f}x expected period-end concentration"
    else:
        sev = "clear"
        head = f"no material period-end clustering (peak {worst:.1f}x expected)"

    return Finding("period_end_cutoff", sev, head, out)


# ----------------------------------------------------------------------------
# 4. Round-number bias
# ----------------------------------------------------------------------------
def round_number_bias(
    txns: pd.DataFrame,
    amount_col: str = "amount",
    base: int = 25_000,
    expected_rate: float = 0.005,
) -> Finding:
    """Flag implausible clusters of perfectly round amounts.

    Real transactional amounts are messy. Round numbers usually mean an
    estimate, an accrual, or a manual journal entry — all of which deserve
    a look, because they are where judgment (and manipulation) lives.
    """
    amt = txns[amount_col].to_numpy()
    is_round = (np.abs(amt % base) < 1e-6) & (amt > 0)
    rate = is_round.mean()

    if rate > expected_rate * 4:
        sev = "high"
    elif rate > expected_rate * 2:
        sev = "medium"
    else:
        sev = "clear"

    head = f"{is_round.sum()} of {len(amt)} amounts ({rate*100:.2f}%) are exact multiples of {base:,}"
    detail = txns.loc[is_round].copy()
    return Finding("round_number_bias", sev, head, detail)


# ----------------------------------------------------------------------------
# 5. Serial "one-off" detection
# ----------------------------------------------------------------------------
def serial_addbacks(
    schedule: pd.DataFrame,
    item_col: str = "item",
    min_years: int = 3,
) -> Finding:
    """Find add-backs claimed as non-recurring that recur.

    This is the single highest-value automated check in QoE, because it is
    purely a question about the data: how many years does this 'one-off'
    appear in? The judgment (will it recur NEXT year?) remains human — but
    an item present in 4 of 5 years carries an obvious burden of proof.
    """
    year_cols = [c for c in schedule.columns if c != item_col]
    df = schedule.copy()
    df["years_present"] = (df[year_cols] > 0).sum(axis=1)
    df["total"] = df[year_cols].sum(axis=1)
    df["is_serial"] = df["years_present"] >= min_years

    # Forward-looking / projected items are a separate, worse category
    projected_mask = df[item_col].str.contains(
        r"run.?rate|synerg|projected|pro.?forma|annualiz", case=False, regex=True
    )
    df["is_projected"] = projected_mask

    serial = df[df["is_serial"]]
    projected = df[df["is_projected"]]

    flagged_value = serial["total"].sum() + projected.loc[~projected["is_serial"], "total"].sum()
    total_value = df["total"].sum()

    if len(projected) or len(serial):
        sev = "high"
        parts = []
        if len(serial):
            parts.append(f"{len(serial)} item(s) recur in >={min_years} years")
        if len(projected):
            parts.append(f"{len(projected)} forward-looking/pro-forma item(s)")
        head = (
            f"{'; '.join(parts)} — {flagged_value:,.0f} of {total_value:,.0f} "
            f"({flagged_value/total_value*100:.0f}%) of claimed add-backs need support"
        )
    else:
        sev = "clear"
        head = "no serial or forward-looking add-backs detected"

    cols = [item_col, "years_present", "total", "is_serial", "is_projected"]
    return Finding("serial_addbacks", sev, head, df[cols].sort_values("total", ascending=False))


# ----------------------------------------------------------------------------
# Orchestration
# ----------------------------------------------------------------------------
def run_all(txns: pd.DataFrame, monthly: pd.DataFrame, addbacks: pd.DataFrame) -> list[Finding]:
    """Run the full forensic battery and return findings ordered by severity."""
    findings = [
        proof_of_cash(monthly),
        period_end_cutoff(txns),
        serial_addbacks(addbacks),
        benford_first_digit(txns["amount"]),
        round_number_bias(txns),
    ]
    order = {"high": 0, "medium": 1, "low": 2, "clear": 3}
    return sorted(findings, key=lambda f: order[f.severity])
