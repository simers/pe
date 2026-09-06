"""
dcf — intrinsic valuation, with the uncertainty made visible.

The central honesty problem with a DCF is that terminal value routinely
accounts for 65-80% of the answer, and terminal value rests on a growth rate
someone guessed. A single-point DCF therefore projects false precision.

The fix is not a better model of the future — no ML helps with year-6-to-
infinity. The fix is to stop pretending you know: run the calculation
thousands of times across plausible assumption ranges and report the
DISTRIBUTION, plus which assumption actually drives the spread (tornado).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class DCFResult:
    enterprise_value: float
    equity_value: float
    pv_explicit: float
    pv_terminal: float
    terminal_share: float
    schedule: pd.DataFrame

    def summary(self) -> str:
        return "\n".join(
            [
                f"PV of explicit forecast   : {self.pv_explicit:,.0f}",
                f"PV of terminal value      : {self.pv_terminal:,.0f}",
                f"Enterprise value          : {self.enterprise_value:,.0f}",
                f"Equity value              : {self.equity_value:,.0f}",
                f"Terminal value share      : {self.terminal_share*100:.0f}%"
                + ("   <-- the answer is mostly an assumption" if self.terminal_share > 0.6 else ""),
            ]
        )


def project_fcf(
    revenue_0: float,
    years: int,
    growth: float | list[float],
    ebitda_margin: float,
    capex_pct: float,
    nwc_pct_of_growth: float,
    tax_rate: float,
    da_pct: float,
) -> pd.DataFrame:
    """Build a free-cash-flow schedule from operating drivers.

    NWC is modelled as a percentage of REVENUE GROWTH, not of revenue — this
    encodes the lesson that working capital is a drag that scales with growth:
    a faster-growing business consumes more cash, which is exactly what makes
    profitable growth companies run short of money.
    """
    g = [growth] * years if isinstance(growth, (int, float)) else list(growth)
    rows = []
    rev = revenue_0
    for t in range(1, years + 1):
        prev_rev = rev
        rev = prev_rev * (1 + g[t - 1])
        ebitda = rev * ebitda_margin
        da = rev * da_pct
        ebit = ebitda - da
        nopat = ebit * (1 - tax_rate)
        capex = rev * capex_pct
        d_nwc = (rev - prev_rev) * nwc_pct_of_growth
        fcf = nopat + da - capex - d_nwc
        rows.append(
            {
                "year": t,
                "revenue": rev,
                "ebitda": ebitda,
                "ebit": ebit,
                "nopat": nopat,
                "capex": capex,
                "change_in_nwc": d_nwc,
                "fcf": fcf,
            }
        )
    return pd.DataFrame(rows)


def value(
    revenue_0: float,
    years: int = 5,
    growth: float | list[float] = 0.08,
    ebitda_margin: float = 0.25,
    capex_pct: float = 0.04,
    nwc_pct_of_growth: float = 0.15,
    tax_rate: float = 0.25,
    da_pct: float = 0.035,
    wacc: float = 0.10,
    terminal_growth: float = 0.02,
    net_debt: float = 0.0,
    terminal_method: str = "perpetuity",
    exit_multiple: float = 10.0,
) -> DCFResult:
    """Discounted cash flow with either a perpetuity or exit-multiple terminal value."""
    if terminal_growth >= wacc:
        raise ValueError(
            f"terminal growth ({terminal_growth:.1%}) must be below WACC ({wacc:.1%}) "
            "— otherwise the perpetuity formula returns a negative or infinite value"
        )

    sched = project_fcf(
        revenue_0, years, growth, ebitda_margin, capex_pct, nwc_pct_of_growth, tax_rate, da_pct
    )
    disc = 1 / (1 + wacc) ** sched["year"].to_numpy()
    sched["discount_factor"] = disc
    sched["pv_fcf"] = sched["fcf"] * disc
    pv_explicit = float(sched["pv_fcf"].sum())

    final_fcf = float(sched["fcf"].iloc[-1])
    if terminal_method == "perpetuity":
        tv = final_fcf * (1 + terminal_growth) / (wacc - terminal_growth)
    elif terminal_method == "exit_multiple":
        tv = float(sched["ebitda"].iloc[-1]) * exit_multiple
    else:
        raise ValueError("terminal_method must be 'perpetuity' or 'exit_multiple'")

    pv_tv = tv / (1 + wacc) ** years
    ev = pv_explicit + pv_tv

    return DCFResult(
        enterprise_value=ev,
        equity_value=ev - net_debt,
        pv_explicit=pv_explicit,
        pv_terminal=pv_tv,
        terminal_share=pv_tv / ev if ev else float("nan"),
        schedule=sched,
    )


def monte_carlo(
    base_kwargs: dict,
    n_sims: int = 10_000,
    dists: dict | None = None,
    seed: int = 11,
) -> pd.DataFrame:
    """Sample the fragile assumptions and report the distribution of value.

    `dists` maps a kwarg name to (mean, std). Defaults perturb the four inputs
    that actually move a DCF: growth, margin, WACC, terminal growth.
    """
    rng = np.random.default_rng(seed)
    dists = dists or {
        "growth": (base_kwargs.get("growth", 0.08), 0.025),
        "ebitda_margin": (base_kwargs.get("ebitda_margin", 0.25), 0.02),
        "wacc": (base_kwargs.get("wacc", 0.10), 0.012),
        "terminal_growth": (base_kwargs.get("terminal_growth", 0.02), 0.006),
    }

    out = []
    for _ in range(n_sims):
        kw = dict(base_kwargs)
        for key, (mu, sd) in dists.items():
            kw[key] = float(rng.normal(mu, sd))
        # keep the model in a valid region
        kw["wacc"] = max(kw["wacc"], 0.04)
        kw["terminal_growth"] = min(kw["terminal_growth"], kw["wacc"] - 0.01)
        kw["ebitda_margin"] = float(np.clip(kw["ebitda_margin"], 0.02, 0.7))
        try:
            r = value(**kw)
            out.append({**{k: kw[k] for k in dists}, "ev": r.enterprise_value})
        except ValueError:
            continue
    return pd.DataFrame(out)


def tornado(base_kwargs: dict, swings: dict | None = None) -> pd.DataFrame:
    """One-at-a-time sensitivity: which assumption actually drives the answer?

    This is the antidote to model theatre. If 70% of your valuation range comes
    from the terminal growth rate, no amount of detail in the year-3 revenue
    build is doing useful work.
    """
    swings = swings or {
        "growth": 0.03,
        "ebitda_margin": 0.03,
        "wacc": 0.015,
        "terminal_growth": 0.01,
        "capex_pct": 0.015,
    }
    base_ev = value(**base_kwargs).enterprise_value

    rows = []
    for key, delta in swings.items():
        lows, highs = [], []
        for sign, bucket in ((-1, lows), (1, highs)):
            kw = dict(base_kwargs)
            kw[key] = base_kwargs.get(key, 0) + sign * delta
            if key == "terminal_growth":
                kw[key] = min(kw[key], kw.get("wacc", 0.10) - 0.01)
            if key == "wacc":
                kw[key] = max(kw[key], kw.get("terminal_growth", 0.02) + 0.01)
            bucket.append(value(**kw).enterprise_value)
        lo, hi = lows[0], highs[0]
        rows.append(
            {
                "assumption": key,
                "swing": f"+/-{delta:.3f}",
                "ev_low": min(lo, hi),
                "ev_high": max(lo, hi),
                "range": abs(hi - lo),
                "pct_of_base": abs(hi - lo) / base_ev,
            }
        )
    return pd.DataFrame(rows).sort_values("range", ascending=False).reset_index(drop=True)
