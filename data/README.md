# Data

This folder is filled when the notebooks run. Its contents are not stored on GitHub.

- `raw/`: files downloaded by `code/01_get_data.ipynb`
- `processed/`: files built by `code/02_clean.ipynb`, `code/03_model.ipynb` and `code/04_volatility.ipynb`

## Licences

- **Yahoo Finance** (currency pairs, S&P 500): Yahoo's terms allow personal use but not
  redistribution, so the files are not included. The download code is in `code/01_get_data.ipynb`.
- **FRED** (exchange rates 1999-2004, interest rates, VIX): most series are free to use; the
  exchange rates are from the Federal Reserve's H.10 release, the interest rates from the OECD,
  and the VIX is the property of Cboe and is cited as such. For consistency, all data is downloaded by code rather than stored here.
