# Project plan

**Title:** Trend Following as Crisis Protection: Evidence from the FX Risk-On/Risk-Off Factor

This file records every design decision **before** any result is seen.
If a decision changes later, the change and the reason are written here, with the date.

---

## 1. The question

Major currency pairs largely move as one factor: risk-on currencies (EUR, GBP, AUD)
against safe havens (JPY, CHF). Holding the risk-on side earns carry in calm markets
but loses in equity crashes.

1. Does following the trend of this factor (long when it rises, short when it falls)
   turn it into protection in equity crashes?
2. Does one learned model (bagging) beat a fixed trend rule, after costs, on unseen data?

Approved by the teaching assistant on 9 October 2026, confirmed by email on 14 November 2026,
with two conditions:
- compare the fixed rule with **one** learned model; add another method only if that one
  visibly fails, and say why;
- define "next period" before starting.

## 2. Fixed decisions

| Decision | Value | Why |
|---|---|---|
| Period | **One week**, Friday close to Friday close | Daily is mostly noise and costly to trade; monthly gives too few observations (about 260) for a learned model. Weekly gives about 1,100. |
| Signal timing | Computed at Friday close, position held the **following** week | Avoids look-ahead: we never trade at the price the signal used. |
| Sample | January 2005 to the last complete week of the download | Longest common history. |
| Holdout | **2024-01-01 onward**, opened once at the very end | Final, untouched test. |
| Factor | Equal-weight basket of all 14 pairs, each held long; weekly return = spot move + one week of carry | Each pair is quoted so that long = risk-on. Net exposure: long EUR, GBP, AUD; short JPY, CHF; USD and CAD cancel. Fixed by currency logic, never fitted to the data. |
| Baseline | Sign of the factor's **52-week** return: long if positive, short if negative | Classic 12-month trend rule. |
| Learned model | **Bagging** of decision trees (scikit-learn) | Can learn combinations of inputs, shows which inputs matter, few settings to tune. |
| Target | Sign of next week's factor return (up = 1, down = 0) | Classification, as taught in week 6. |
| Inputs | Factor return over 1, 4, 13 and 52 weeks; carry (3-month rate of risk-on minus safe-haven currencies); VIX level and its 4-week change | Trend at several horizons, plus carry and fear. |
| Position from the model | Long if predicted probability of "up" > 0.5, short otherwise | Simple and symmetric. |
| Evaluation scheme | Walk-forward, expanding window: train on all years before year Y, test on year Y. First test year 2010. | Train only on the past, as in real life. |
| Tuning | Number of trees and tree depth chosen on the last 2 years of each training window only | Never tune on the test data. |
| Costs | 3 basis points per unit of position change | Typical spread on major pairs; doubled in a robustness check. |
| Random seed | 42 | Same numbers on every run. |

### The 14 pairs

CADJPY, AUDUSD, USDJPY, EURUSD, EURCHF, GBPJPY, USDCAD, GBPUSD, EURGBP, GBPCHF, CHFJPY, AUDJPY, EURJPY, USDCHF

Net exposure per unit invested: EUR +0.29, GBP +0.14, AUD +0.14, CHF -0.14, JPY -0.43, USD 0, CAD 0.
Carry of the basket = exposure-weighted 3-month rate (percent per year).

## 3. Pipeline: what each notebook loads, does and saves

| Notebook | Loads | Does | Saves |
|---|---|---|---|
| `code/01_get_data.ipynb` | internet (Yahoo, FRED) | Downloads all raw series | `data/raw/*.csv` |
| `code/02_clean.ipynb` | `data/raw/` | Aligns dates, drops unfinished days, rebuilds AUDUSD 2005 to 2006, lags monthly rates, builds weekly series and the factor | `data/processed/weekly.csv` |
| `code/03_model.ipynb` | `data/processed/weekly.csv` | Baseline rule and bagging, walk-forward, costs | `data/processed/positions.csv` |
| `code/04_figures.ipynb` | `data/processed/` | All figures and tables for the paper, crash analysis, robustness | `figures/*.png` |

Shared functions (used in more than one notebook) live in `code/helpers.py`.

## 4. Checks each stage must pass before moving on

**01_get_data**
- Every series downloaded, none empty.
- First and last dates printed.

**02_clean**
- No missing values in the weekly table.
- No date after the download date; the last week is complete.
- Rebuilt AUDUSD (AUDJPY / USDJPY) matches the real AUDUSD after May 2006 (correlation of weekly returns above 0.99).
- Monthly rates are lagged so a value is only used after it was published.
- The factor falls in late 2008 and March 2020 (risk-off), as expected.

**03_model**
- Every signal is shifted by one week (no look-ahead).
- No holdout data (2024 onward) used in training or tuning.
- Training accuracy much higher than test accuracy is flagged (overfitting alarm).
- Shuffled-target test: with random targets, the model should do no better than a coin flip.

**04_figures**
- Every figure in the paper is produced here.
- Results reported with and without 2008, with and without 2022, and with doubled costs.

## 5. Decisions for stage 2 (settled 2026-11-14)

- Three FRED series stop in January 2026 (EUR 3m, EUR 10y, GBP 3m): the last value is
  carried forward. It affects about 10 months out of 21 years; stated in the paper.
- Publication lag for monthly rates: **2 months** (a value dated August is used from October).
- Weekly series use the **Friday close**; if Friday is missing, the last available day of that week.
- Unfinished days (on or after the download date in `data/raw/download_date.txt`) are dropped.
- One-day price errors in the Yahoo data (a move above 3% that is at least 70% reversed the
  next day) are removed and replaced by the previous price. 36 such days were found.

## 5b. Decisions for stages 3 and 4 (settled 2026-11-14)

- Baseline signal: sign of the **total** factor return (spot + carry) over the last 52 weeks.
- The model is retrained **once a year**, in January: train on all weeks before year Y, test on year Y.
- Tuning grid: number of trees 100 or 300; maximum tree depth 2, 3 or 5 (6 combinations).
  Each combination is scored by accuracy on the last 2 years of the training window; the best
  is refit on the full training window.
- Costs: 3 bp per unit of position change (long to short = 2 units = 6 bp).
- Test years 2010 to 2023. Weeks from 2024-01-01 (holdout) are dropped at the start of the notebook.
- Robustness to add in stage 5: rerun with the one-day price error rule switched off.

## 6. Change log

| Date | Change | Reason |
|---|---|---|
| 2026-11-14 | Plan written | Proposal approved |
| 2026-11-14 | Stage 2 decisions settled (section 5) | Before writing the cleaning code |
| 2026-11-14 | Factor redefined as the equal-weight basket of all 14 pairs held long | The two groups of 7 pairs have identical currency exposure, so "buy minus sell" is zero by construction. Found while checking the factor in stage 2, before any model was run. |
| 2026-11-14 | One-day price error rule added to stage 2 | Yahoo FX history contains bad prints (e.g. EURUSD +17% on 8 Dec 2008, reversed next day). |
| 2026-11-14 | Stage 3 and 4 decisions settled (section 5b) | Before writing the model code |
