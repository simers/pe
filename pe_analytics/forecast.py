"""
forecast — driver forecasting, scored honestly.

This module exists to answer a specific question: can a model predict revenue
or margin better than a naive rule? Most published financial ML skips this
comparison, which is why so much of it is worthless — a model that fails to
beat "next quarter looks like this quarter" has produced nothing.

Two guardrails are enforced:

  WALK-FORWARD VALIDATION. Time-series data must never be shuffled into a
  random train/test split. Doing so lets the model learn from the future to
  predict the past, producing accuracy that evaporates in production.

  BASELINE COMPARISON. Every model is scored against naive-last-value and
  linear-trend benchmarks. If it doesn't win, `verdict` says so plainly.

Model choice: gradient boosting on lagged features. With ~28 quarterly
observations, a deep network has far more parameters than data points and
would simply memorize. Boosted trees on engineered lags are the right
complexity here — and if even they can't beat a trend line, that is the
finding, not a failure.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor


@dataclass
class BacktestResult:
    model_mae: float
    naive_mae: float
    trend_mae: float
    n_test: int
    predictions: pd.DataFrame

    @property
    def beats_naive(self) -> bool:
        return self.model_mae < self.naive_mae

    @property
    def improvement(self) -> float:
        return (self.naive_mae - self.model_mae) / self.naive_mae

    def verdict(self) -> str:
        best_baseline = min(self.naive_mae, self.trend_mae)
        name = "naive" if self.naive_mae <= self.trend_mae else "trend"
        if self.model_mae < best_baseline:
            return (
                f"MODEL WINS: MAE {self.model_mae:.2f} vs best baseline "
                f"({name}) {best_baseline:.2f} — {(best_baseline-self.model_mae)/best_baseline*100:.0f}% better"
            )
        return (
            f"MODEL LOSES: MAE {self.model_mae:.2f} vs best baseline ({name}) "
            f"{best_baseline:.2f}. Use the baseline. A model that cannot beat a "
            f"simple rule adds cost and false confidence, not insight."
        )

    def summary(self) -> str:
        return "\n".join(
            [
                f"Test observations         : {self.n_test}",
                f"Naive (last value)   MAE  : {self.naive_mae:.2f}",
                f"Linear trend         MAE  : {self.trend_mae:.2f}",
                f"Gradient boosting    MAE  : {self.model_mae:.2f}",
                f"-> {self.verdict()}",
            ]
        )


def make_lag_features(series: np.ndarray, n_lags: int = 4) -> tuple[np.ndarray, np.ndarray]:
    """Build a supervised dataset of [t-1..t-n_lags] -> t."""
    X, y = [], []
    for i in range(n_lags, len(series)):
        X.append(series[i - n_lags : i])
        y.append(series[i])
    return np.array(X), np.array(y)


def walk_forward(
    series: pd.Series | np.ndarray,
    n_lags: int = 4,
    min_train: int = 12,
    seed: int = 3,
) -> BacktestResult:
    """Expanding-window walk-forward backtest against two naive baselines.

    At each step the model trains only on data available up to that point,
    then predicts one step ahead — the honest simulation of live use.
    """
    s = np.asarray(pd.Series(series).astype(float))
    X, y = make_lag_features(s, n_lags)
    if len(y) <= min_train + 2:
        raise ValueError(
            f"need more history: {len(y)} supervised rows after lagging, "
            f"min_train={min_train}. Short series should use a trend, not a model."
        )

    preds, naive, trend, actual = [], [], [], []
    for i in range(min_train, len(y)):
        Xtr, ytr = X[:i], y[:i]
        model = GradientBoostingRegressor(
            n_estimators=200, max_depth=2, learning_rate=0.05, random_state=seed
        )
        model.fit(Xtr, ytr)
        preds.append(float(model.predict(X[i : i + 1])[0]))

        # Baseline 1: next value = last value
        naive.append(float(X[i][-1]))
        # Baseline 2: linear trend fit on the training window
        t = np.arange(len(ytr))
        b = np.polyfit(t, ytr, 1)
        trend.append(float(np.polyval(b, len(ytr))))

        actual.append(float(y[i]))

    a = np.array(actual)
    out = pd.DataFrame(
        {"actual": a, "model": preds, "naive_last": naive, "linear_trend": trend}
    )
    return BacktestResult(
        model_mae=float(np.abs(a - np.array(preds)).mean()),
        naive_mae=float(np.abs(a - np.array(naive)).mean()),
        trend_mae=float(np.abs(a - np.array(trend)).mean()),
        n_test=len(a),
        predictions=out,
    )


def forecast_forward(
    series: pd.Series | np.ndarray,
    periods: int = 4,
    n_lags: int = 4,
    seed: int = 3,
) -> np.ndarray:
    """Recursive multi-step forecast.

    Caveat worth stating out loud: recursive forecasting compounds error —
    each step feeds its own prediction back as an input. Treat period 4 with
    considerably less confidence than period 1.
    """
    s = list(np.asarray(pd.Series(series).astype(float)))
    X, y = make_lag_features(np.array(s), n_lags)
    model = GradientBoostingRegressor(
        n_estimators=200, max_depth=2, learning_rate=0.05, random_state=seed
    )
    model.fit(X, y)

    out = []
    for _ in range(periods):
        nxt = float(model.predict(np.array(s[-n_lags:]).reshape(1, -1))[0])
        out.append(nxt)
        s.append(nxt)
    return np.array(out)
