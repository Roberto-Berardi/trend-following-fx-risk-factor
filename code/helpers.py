# Settings and small functions used by more than one notebook.

import numpy as np

# Folders (relative to the code/ folder, where the notebooks live)
RAW = "../data/raw"
PROCESSED = "../data/processed"
FIGURES = "../figures"

# The 14 pairs of the basket
BUY_PAIRS = ["CADJPY", "AUDUSD", "USDJPY", "EURUSD", "EURCHF", "GBPJPY", "USDCAD"]
SELL_PAIRS = ["GBPUSD", "EURGBP", "GBPCHF", "CHFJPY", "AUDJPY", "EURJPY", "USDCHF"]
ALL_PAIRS = BUY_PAIRS + SELL_PAIRS

# FRED series: 3-month and 10-year rates for each currency, and the VIX
FRED_SERIES = {
    "USD_3M": "IR3TIB01USM156N", "USD_10Y": "IRLTLT01USM156N",
    "EUR_3M": "IR3TIB01EZM156N", "EUR_10Y": "IRLTLT01EZM156N",
    "GBP_3M": "IR3TIB01GBM156N", "GBP_10Y": "IRLTLT01GBM156N",
    "JPY_3M": "IR3TIB01JPM156N", "JPY_10Y": "IRLTLT01JPM156N",
    "CHF_3M": "IR3TIB01CHM156N", "CHF_10Y": "IRLTLT01CHM156N",
    "AUD_3M": "IR3TIB01AUM156N", "AUD_10Y": "IRLTLT01AUM156N",
    "CAD_3M": "IR3TIB01CAM156N", "CAD_10Y": "IRLTLT01CAM156N",
    "VIX": "VIXCLS",
}

# Fixed choices (see PLAN.md)
START = "2005-01-01"
HOLDOUT_START = "2024-01-01"
FIRST_TEST_YEAR = 2010
# Last year used in testing. 2023 until the holdout is opened, once, at the very end.
LAST_TEST_YEAR = 2023
COST_BP = 3          # cost in basis points per unit of position change
SEED = 42
WEEKS_PER_YEAR = 52


def sharpe_ratio(weekly_returns):
    # Annualised Sharpe ratio from weekly returns
    return weekly_returns.mean() / weekly_returns.std() * np.sqrt(WEEKS_PER_YEAR)


def max_drawdown(weekly_returns):
    # Largest fall from a previous peak of the cumulative return
    wealth = (1 + weekly_returns).cumprod()
    peak = wealth.cummax()
    return (wealth / peak - 1).min()
