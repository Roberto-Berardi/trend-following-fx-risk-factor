# Trend Following as Crisis Protection: Evidence from the FX Risk-On/Risk-Off Factor

Advanced Data Analytics, HEC Lausanne, autumn 2026. Roberto Berardi.

## What this project does

Major currency pairs largely move as one factor: risk-on currencies (EUR, GBP, AUD) against the
safe havens (JPY, CHF). Holding the risk-on side earns carry in calm markets but loses in equity
crashes. This project asks whether following the factor's trend turns it into crisis protection,
and whether machine learning beats a fixed trend rule, judged from the point of view of a Swiss
investor holding 100,000 CHF of the S&P 500.

The fixed 52-week trend rule is compared with a learned direction model (bagging). The bagging
model cannot predict direction, so the next step forecasts next week's volatility instead (linear
regression and a Gaussian process, with GARCH as a benchmark). The forecasts size the positions
and feed the risk tests (VaR and a risk budget), and a Gaussian mixture labels market regimes.
All models are evaluated walk-forward on the test years 2007 to 2026. The last three years
(2024 to 2026) were held out and opened only once, at the end.

## How to run it

1. Install the packages:
   ```
   pip install -r requirements.txt
   ```
2. Run the notebooks in `code/`, in order, each from top to bottom (restart the kernel first):
   1. `01_get_data.ipynb` downloads the data into `data/raw/`
   2. `02_clean.ipynb` builds the weekly data set in `data/processed/`
   3. `03_model.ipynb` runs the trend rule and the direction model (bagging)
   4. `04_volatility.ipynb` forecasts volatility, finds market regimes, builds the strategies and
      the risk-management tests (VaR, risk budget)
   5. `05_figures.ipynb` produces every figure and table in `figures/`, with the statistical tests

Run time: about 10 minutes in total in the Nuvolos workspace, most of it in `04_volatility.ipynb`.

All settings (sample, test years, costs, random seed) are in `code/helpers.py`.

## Data

- Daily prices of 14 currency pairs (2005 onward) and the S&P 500 (1999 onward): Yahoo Finance,
  through the `yfinance` package.
- Daily exchange rates against the US dollar, 1999 to 2004 (training history before Yahoo starts):
  FRED, Federal Reserve Bank of St. Louis (H.10 noon rates).
- Short- and long-term interest rates, overnight rates and the VIX: FRED.

Weekly data, Friday close. The sample ends on Friday 13 November 2026 (fixed in `code/helpers.py`),
so a later download gives the same weeks.

The data files are not stored in this repository (see `data/README.md`). The first notebook downloads them.

## Files

- `code/`: one notebook per stage, plus `helpers.py` for shared settings and functions
- `data/`: downloaded and processed data (created when the notebooks run)
- `figures/`: figures used in the paper
- `paper.pdf`: the paper (added at the end)
