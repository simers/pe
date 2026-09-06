"""
run_demo — end-to-end walkthrough on synthetic data with planted issues.

Run:  python3 -m pe_analytics.run_demo
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from . import comps, dcf, demo_data, forecast, qoe_forensics

pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 20)


def rule(title: str) -> None:
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def main() -> None:
    # ------------------------------------------------------------------ QoE
    rule("1. QUALITY OF EARNINGS — forensic screen")
    txns = demo_data.transactions()
    monthly = demo_data.monthly_financials(txns)
    addbacks = demo_data.addback_schedule()

    findings = qoe_forensics.run_all(txns, monthly, addbacks)
    for f in findings:
        print(f)

    print("\nSerial add-back detail (the highest-value automated check):")
    detail = next(f for f in findings if f.check == "serial_addbacks").detail
    print(detail.to_string(index=False))

    print("\nPeriod-end concentration by quarter (last 6):")
    cut = next(f for f in findings if f.check == "period_end_cutoff").detail
    print(cut.tail(6).to_string(index=False))

    # ---------------------------------------------------------------- Comps
    rule("2. COMPARABLES — extrinsic valuation")
    universe = demo_data.comps_table()
    target_ebitda, target_growth, target_margin = 175.0, 0.10, 0.235

    res = comps.value(universe, target_ebitda, target_growth, target_margin)
    print(f"Target: EBITDA {target_ebitda:.0f}, growth {target_growth:.0%}, margin {target_margin:.1%}\n")
    print(res.summary())

    # ------------------------------------------------------------------ DCF
    rule("3. DCF — intrinsic valuation with uncertainty")
    base = dict(
        revenue_0=745.0,
        years=5,
        growth=0.09,
        ebitda_margin=0.235,
        capex_pct=0.04,
        nwc_pct_of_growth=0.15,
        tax_rate=0.25,
        da_pct=0.035,
        wacc=0.105,
        terminal_growth=0.025,
        net_debt=250.0,
    )
    d = dcf.value(**base)
    print(d.summary())

    print("\nTornado — which assumption actually drives the answer:")
    t = dcf.tornado(base)
    t_show = t.assign(
        ev_low=lambda x: x.ev_low.round(0),
        ev_high=lambda x: x.ev_high.round(0),
        range=lambda x: x["range"].round(0),
        pct_of_base=lambda x: (x.pct_of_base * 100).round(1).astype(str) + "%",
    )
    print(t_show.to_string(index=False))

    print("\nMonte Carlo (10,000 sims) — the distribution, not a point estimate:")
    mc = dcf.monte_carlo(base, n_sims=10_000)
    q = mc["ev"].quantile([0.05, 0.25, 0.50, 0.75, 0.95])
    for k, v in q.items():
        print(f"  P{int(k*100):<3d} enterprise value : {v:>12,.0f}")
    print(f"  Probability EV exceeds comps midpoint ({res.implied_ev_median:,.0f}): "
          f"{(mc['ev'] > res.implied_ev_median).mean()*100:.0f}%")

    # ------------------------------------------------------------- Forecast
    rule("4. FORECASTING — does the model beat a naive rule?")
    hist = demo_data.driver_history()
    bt = forecast.walk_forward(hist["revenue"], n_lags=4, min_train=12)
    print(bt.summary())

    nxt = forecast.forecast_forward(hist["revenue"], periods=4)
    print("\nNext 4 quarters (recursive — error compounds, trust Q1 most):")
    for i, v in enumerate(nxt, 1):
        print(f"  Q+{i}: {v:,.1f}")

    # ------------------------------------------------------------- Synthesis
    rule("5. THE FOOTBALL FIELD")
    lo = min(res.low_ev, mc["ev"].quantile(0.25))
    hi = max(res.high_ev, mc["ev"].quantile(0.75))
    print(f"  Comps (IQR + regression band) : {res.low_ev:>12,.0f} - {res.high_ev:,.0f}")
    print(f"  DCF (Monte Carlo P25-P75)     : {mc['ev'].quantile(0.25):>12,.0f} - {mc['ev'].quantile(0.75):,.0f}")
    print(f"  Overlap / convergence zone    : {lo:>12,.0f} - {hi:,.0f}")
    print("\n  Note: an LBO ceiling (max price at target IRR) would normally sit")
    print("  below both — that is Module 4/5 and belongs in the model workbook.")

    print("\nEvery number above is a FLAG or a RANGE for a human to interrogate.")
    print("None of it decides whether an add-back is legitimate — that is judgment.")


if __name__ == "__main__":
    main()
