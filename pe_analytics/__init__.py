"""
pe_analytics — forensic diligence & valuation tooling for private equity.

DESIGN PRINCIPLES (deliberate, and they shape every module):

1. FLAGS, NOT VERDICTS.  Every detector returns exceptions for a human to
   investigate. Nothing here decides whether an add-back is legitimate —
   that is a forward-looking judgment about the business, not a property
   of the data.

2. BEAT THE BASELINE OR ADMIT IT.  Any predictive model is scored against
   a naive benchmark (last value / simple trend). If it doesn't beat the
   baseline, the code says so rather than quietly reporting an R-squared.

3. NO LOOK-AHEAD.  Time-series validation is walk-forward. We never shuffle
   dated rows into a random train/test split — that leaks the future and
   produces flattering, useless accuracy.

4. SMALL-n HONESTY.  Comps sets are 8-15 rows, not 8 million. Modules
   refuse to fit when n is too small and report confidence intervals
   rather than point estimates.

5. INTERPRETABILITY OVER RAW FIT.  A number you must defend across a
   negotiating table needs a mechanism, not just a prediction.

Modules
-------
demo_data      synthetic GL / financials / comps so everything runs out of the box
qoe_forensics  proof of cash, Benford, cutoff testing, round-number bias, serial add-backs
comps          peer multiples with regression adjustment and honest uncertainty
dcf            DCF with Monte Carlo and tornado sensitivity on the fragile inputs
forecast       driver forecasting with walk-forward validation vs naive baselines
"""

__version__ = "0.1.0"

__all__ = ["demo_data", "qoe_forensics", "comps", "dcf", "forecast"]
