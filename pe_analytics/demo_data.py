"""
demo_data — synthetic but realistic diligence data, with issues deliberately planted.

Planted problems (so you can verify the detectors actually catch things):
  * CHANNEL STUFFING   — revenue spikes in the last 3 days of each quarter,
                         growing worse in the final year (the measurement period).
  * PROOF-OF-CASH GAP  — recognized revenue exceeds bank deposits in later months
                         (revenue booked that never turned into cash).
  * SERIAL ONE-OFFS    — "restructuring" added back in 4 of 5 years.
  * ROUND-NUMBER BIAS  — a cluster of suspiciously round manual journal entries.

Everything is reproducible via `seed`.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def transactions(n: int = 6000, seed: int = 7) -> pd.DataFrame:
    """Revenue-transaction level general ledger for 3 fiscal years."""
    rng = np.random.default_rng(seed)

    start = pd.Timestamp("2023-01-01")
    end = pd.Timestamp("2025-12-31")
    span = (end - start).days

    # Base population: lognormal amounts (realistic invoice-size skew)
    days = rng.integers(0, span, size=n)
    dates = start + pd.to_timedelta(days, unit="D")
    amounts = np.exp(rng.normal(8.6, 0.9, size=n))  # ~$5k median invoice

    df = pd.DataFrame({"date": dates, "amount": amounts})
    df["source"] = "auto"

    # --- PLANT 1: channel stuffing in the last 3 days of each quarter -------
    stuff = []
    for year, intensity in [(2023, 12), (2024, 22), (2025, 55)]:  # worsening
        for month in (3, 6, 9, 12):
            q_end = pd.Timestamp(year=year, month=month, day=1) + pd.offsets.MonthEnd(0)
            for _ in range(intensity):
                stuff.append(
                    {
                        "date": q_end - pd.Timedelta(days=int(rng.integers(0, 3))),
                        "amount": float(np.exp(rng.normal(9.4, 0.7))),  # larger deals
                        "source": "manual",
                    }
                )
    df = pd.concat([df, pd.DataFrame(stuff)], ignore_index=True)

    # --- PLANT 2: round-number manual journal entries -----------------------
    round_je = pd.DataFrame(
        {
            "date": start + pd.to_timedelta(rng.integers(0, span, size=90), unit="D"),
            "amount": rng.choice([25_000, 50_000, 75_000, 100_000, 250_000], size=90).astype(float),
            "source": "manual",
        }
    )
    df = pd.concat([df, round_je], ignore_index=True)

    return df.sort_values("date").reset_index(drop=True)


def monthly_financials(txns: pd.DataFrame, seed: int = 7) -> pd.DataFrame:
    """Monthly recognized revenue vs cash actually deposited.

    Deposits track revenue early on, then fall behind — the proof-of-cash gap.
    """
    rng = np.random.default_rng(seed + 1)

    rev = (
        txns.assign(period=txns["date"].dt.to_period("M"))
        .groupby("period")["amount"]
        .sum()
        .rename("revenue_recognized")
        .to_frame()
    )
    rev.index = rev.index.to_timestamp()

    n = len(rev)
    # Collection ratio decays from ~1.00 to ~0.88 across the period
    drift = np.linspace(1.00, 0.88, n)
    noise = rng.normal(0, 0.02, n)
    rev["cash_deposits"] = rev["revenue_recognized"].to_numpy() * (drift + noise)

    return rev.reset_index(names="month")


def addback_schedule() -> pd.DataFrame:
    """Seller-proposed add-backs by year ($000s). Note the serial 'one-off'."""
    return pd.DataFrame(
        [
            # item,                       2021,  2022,  2023,  2024,  2025
            ("Restructuring charges",     1200,  900,      0,  1450,  1310),
            ("Legal settlement",             0,     0,   2600,     0,     0),
            ("Owner compensation adj.",    380,   395,    410,   425,   440),
            ("M&A transaction fees",         0,  1750,      0,     0,   980),
            ("Management fees (sponsor)",  600,   600,    600,   600,   600),
            ("Run-rate synergies (proj.)",   0,     0,      0,     0,  3400),
            ("Facility relocation",          0,     0,      0,   720,     0),
        ],
        columns=["item", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025"],
    )


def comps_table() -> pd.DataFrame:
    """Trading comparables. Multiples correlate with growth and margin (as they should)."""
    return pd.DataFrame(
        [
            # name,        ev_musd, ebitda_musd, rev_growth, ebitda_margin
            ("Comp A",        2100,        210,       0.06,          0.22),
            ("Comp B",        3400,        295,       0.11,          0.26),
            ("Comp C",         890,         98,       0.03,          0.19),
            ("Comp D",        5600,        430,       0.15,          0.29),
            ("Comp E",        1450,        160,       0.05,          0.21),
            ("Comp F",        4100,        330,       0.13,          0.27),
            ("Comp G",        1150,        135,       0.04,          0.20),
            ("Comp H",        2950,        250,       0.09,          0.24),
            ("Comp I",         720,         88,       0.02,          0.18),
            ("Comp J",        6200,        455,       0.17,          0.31),
            ("Comp K",        1880,        190,       0.07,          0.23),
            ("Comp L",        2600,        240,       0.08,          0.25),
        ],
        columns=["name", "ev", "ebitda", "rev_growth", "ebitda_margin"],
    ).assign(ev_ebitda=lambda d: d["ev"] / d["ebitda"])


def driver_history(seed: int = 7) -> pd.DataFrame:
    """Quarterly operating history for forecasting (with a real seasonal pattern)."""
    rng = np.random.default_rng(seed + 2)
    q = pd.period_range("2019Q1", "2025Q4", freq="Q")
    t = np.arange(len(q))

    trend = 40.0 * (1.018 ** t)                    # ~7.4%/yr underlying growth
    season = 1 + 0.08 * np.sin(2 * np.pi * (t % 4) / 4 + 0.9)
    shock = np.where((t >= 4) & (t <= 7), 0.90, 1.0)   # 2020 covid dip
    revenue = trend * season * shock * (1 + rng.normal(0, 0.025, len(q)))

    margin = 0.20 + 0.004 * np.log1p(t) + rng.normal(0, 0.008, len(q))

    return pd.DataFrame(
        {
            "quarter": q.astype(str),
            "revenue": revenue.round(2),
            "ebitda_margin": margin.round(4),
            "ebitda": (revenue * margin).round(2),
        }
    )
