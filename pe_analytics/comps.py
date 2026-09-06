"""
comps — extrinsic (relative) valuation done with honest uncertainty.

The naive approach takes the median peer multiple and applies it. That throws
away the most useful information in the table: peers do not trade at the same
multiple, and the DIFFERENCES are systematic — faster-growing, higher-margin
companies trade higher, for reasons anyone can articulate.

So we do two things:
  1. Regress EV/EBITDA on growth and margin, then predict the multiple the
     TARGET's own fundamentals justify. This is defensible in a negotiation
     because it has a mechanism, not just a peer average.
  2. Report a RANGE with a prediction interval, because with n=12 a point
     estimate is false precision.

Why not a neural net: with 12 observations and 2 features, any flexible model
memorizes the table. OLS is the right complexity for the data you actually have.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

MIN_PEERS = 6          # below this, regression is meaningless
COMFORTABLE_PEERS = 10  # below this, warn


@dataclass
class CompsResult:
    median_multiple: float
    regression_multiple: float | None
    implied_ev_median: float
    implied_ev_regression: float | None
    low_ev: float
    high_ev: float
    r_squared: float | None
    n_peers: int
    warnings: list[str]
    coefficients: dict | None = None

    def summary(self) -> str:
        lines = [
            f"Peers used                : {self.n_peers}",
            f"Median peer multiple      : {self.median_multiple:.1f}x",
        ]
        if self.regression_multiple is not None:
            lines += [
                f"Regression-implied mult.  : {self.regression_multiple:.1f}x  (R2={self.r_squared:.2f})",
                f"  driver coefficients     : "
                + ", ".join(f"{k}={v:+.1f}" for k, v in self.coefficients.items()),
            ]
        lines += [
            f"Implied EV (median)       : {self.implied_ev_median:,.0f}",
        ]
        if self.implied_ev_regression is not None:
            lines.append(f"Implied EV (regression)   : {self.implied_ev_regression:,.0f}")
        lines.append(f"Defensible EV range       : {self.low_ev:,.0f} - {self.high_ev:,.0f}")
        for w in self.warnings:
            lines.append(f"  ! {w}")
        return "\n".join(lines)


def select_peers(
    universe: pd.DataFrame,
    target_ebitda: float,
    size_band: tuple[float, float] = (0.25, 4.0),
    ebitda_col: str = "ebitda",
) -> pd.DataFrame:
    """Filter a universe to peers of comparable size.

    Size screening matters because multiples are size-dependent (scale
    premium): a $90M-EBITDA company and a $450M one are not comparables
    just because they share an industry.
    """
    lo, hi = target_ebitda * size_band[0], target_ebitda * size_band[1]
    return universe[(universe[ebitda_col] >= lo) & (universe[ebitda_col] <= hi)].copy()


def regression_adjusted(
    peers: pd.DataFrame,
    target_growth: float,
    target_margin: float,
    multiple_col: str = "ev_ebitda",
    drivers: tuple[str, ...] = ("rev_growth", "ebitda_margin"),
) -> tuple[float | None, float | None, dict | None, float]:
    """OLS of multiple on fundamental drivers; predict the target's multiple.

    Returns (predicted_multiple, r_squared, coefficients, residual_std).
    """
    n = len(peers)
    if n < MIN_PEERS:
        return None, None, None, float("nan")

    X = peers[list(drivers)].to_numpy(dtype=float)
    y = peers[multiple_col].to_numpy(dtype=float)
    A = np.column_stack([np.ones(n), X])

    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    fitted = A @ beta
    resid = y - fitted
    ss_res = float((resid**2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")

    dof = max(n - len(beta), 1)
    resid_std = float(np.sqrt(ss_res / dof))

    target_row = np.array([1.0, target_growth, target_margin])
    predicted = float(target_row @ beta)

    coeffs = {d: float(b) for d, b in zip(drivers, beta[1:])}
    coeffs["intercept"] = float(beta[0])
    return predicted, r2, coeffs, resid_std


def value(
    universe: pd.DataFrame,
    target_ebitda: float,
    target_growth: float,
    target_margin: float,
    apply_size_screen: bool = True,
) -> CompsResult:
    """Full comps valuation with both median and regression approaches."""
    warnings: list[str] = []

    peers = select_peers(universe, target_ebitda) if apply_size_screen else universe.copy()
    if len(peers) < MIN_PEERS:
        warnings.append(
            f"size screen left only {len(peers)} peers — screen relaxed to the full universe"
        )
        peers = universe.copy()

    n = len(peers)
    if n < COMFORTABLE_PEERS:
        warnings.append(f"only {n} peers — treat the range as indicative, not precise")

    median_mult = float(peers["ev_ebitda"].median())
    implied_median = median_mult * target_ebitda

    pred, r2, coeffs, resid_std = regression_adjusted(peers, target_growth, target_margin)

    implied_reg = None
    if pred is not None:
        implied_reg = pred * target_ebitda
        if r2 is not None and r2 < 0.5:
            warnings.append(
                f"regression explains only {r2*100:.0f}% of multiple variation — "
                "the drivers chosen may not be what this market prices on"
            )
        # Is the target outside the peer envelope? Then we're extrapolating.
        if not (peers["rev_growth"].min() <= target_growth <= peers["rev_growth"].max()):
            warnings.append("target growth is outside the peer range — regression is extrapolating")
        if not (peers["ebitda_margin"].min() <= target_margin <= peers["ebitda_margin"].max()):
            warnings.append("target margin is outside the peer range — regression is extrapolating")

    # Range: interquartile peer multiples, widened by regression uncertainty
    q1, q3 = peers["ev_ebitda"].quantile([0.25, 0.75])
    lo_mult, hi_mult = float(q1), float(q3)
    if pred is not None and np.isfinite(resid_std):
        lo_mult = min(lo_mult, pred - resid_std)
        hi_mult = max(hi_mult, pred + resid_std)

    return CompsResult(
        median_multiple=median_mult,
        regression_multiple=pred,
        implied_ev_median=implied_median,
        implied_ev_regression=implied_reg,
        low_ev=lo_mult * target_ebitda,
        high_ev=hi_mult * target_ebitda,
        r_squared=r2,
        n_peers=n,
        warnings=warnings,
        coefficients=coeffs,
    )
