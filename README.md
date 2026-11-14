# Trend Following as Crisis Protection: Evidence from the FX Risk-On/Risk-Off Factor

Advanced Data Analytics, HEC Lausanne, autumn 2026. Roberto Berardi.

## What this project does

Major currency pairs largely move as one factor: risk-on currencies (EUR, GBP, AUD) against
safe havens (JPY, CHF). This project tests whether following the trend of that factor protects
an investor during equity crashes, and whether a learned model (bagging) beats a fixed trend rule.

## How to run it

1. Install the packages:
   ```
   pip install -r requirements.txt
   ```
2. Run the notebooks in `code/`, in order, each from top to bottom:
   1. `01_get_data.ipynb` downloads the data into `data/raw/`
   2. `02_clean.ipynb` builds the weekly data set in `data/processed/`
   3. `03_model.ipynb` runs the trend rule and the model
   4. `04_figures.ipynb` produces every figure and table in `figures/`

Run time: to be measured (expected a few minutes in total).

## Data

- Daily prices of 14 currency pairs and the S&P 500: Yahoo Finance, through the `yfinance` package.
- Short- and long-term interest rates and the VIX: FRED, Federal Reserve Bank of St. Louis.

The data files are not stored in this repository (see `data/README.md`). The first notebook downloads them.

## Files

- `PLAN.md`: every design decision, fixed before any result was seen
- `code/`: one notebook per stage, plus `helpers.py`
- `data/`: downloaded and processed data (created when the notebooks run)
- `figures/`: figures used in the paper
- `paper.pdf`: the paper (added at the end)
