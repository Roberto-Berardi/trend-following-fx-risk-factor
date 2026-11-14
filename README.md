# Trend Following as Crisis Protection: Evidence from the FX Risk-On/Risk-Off Factor

Advanced Data Analytics, HEC Lausanne, autumn 2026. Roberto Berardi.

## What this project does

A Swiss investor holding US equities loses twice in a crisis: on the stocks, and on the dollar as the
franc rises. Major currency pairs largely move as one factor (risk-on currencies EUR, GBP, AUD against
the safe havens JPY and CHF), and that factor falls in the same episodes.

This project tests whether a rules-based FX strategy on that factor, run on top of a 100,000 CHF
S&P 500 portfolio, reduces crisis losses at an acceptable cost in normal times. It compares a simple
trend rule with machine learning models (bagging, linear regression, Gaussian process, Gaussian
mixture regimes, PCA), evaluated out of sample.

## How to run it

1. Install the packages:
   ```
   pip install -r requirements.txt
   ```
2. Run the notebooks in `code/`, in order, each from top to bottom:
   1. `01_get_data.ipynb` downloads the data into `data/raw/`
   2. `02_clean.ipynb` builds the weekly data set in `data/processed/`
   3. `03_model.ipynb` runs the trend rule and the direction model (bagging)
   4. `04_volatility.ipynb` forecasts volatility, finds market regimes and builds the FX overlay
   5. `05_figures.ipynb` produces every figure and table in `figures/`

Run time: to be measured (expected a few minutes in total).

## Data

- Daily prices of 14 currency pairs and the S&P 500: Yahoo Finance, through the `yfinance` package.
- Short- and long-term interest rates and the VIX: FRED, Federal Reserve Bank of St. Louis.

The data files are not stored in this repository (see `data/README.md`). The first notebook downloads them.

## Files

- `code/`: one notebook per stage, plus `helpers.py` for shared settings and functions
- `data/`: downloaded and processed data (created when the notebooks run)
- `figures/`: figures used in the paper
- `paper.pdf`: the paper (added at the end)
