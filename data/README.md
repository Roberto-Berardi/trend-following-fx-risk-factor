# Data

This folder is filled when the notebooks run. Its contents are not stored on GitHub.

- `raw/`: files downloaded by `code/01_get_data.ipynb`
- `processed/`: files built by `code/02_clean.ipynb` and `code/03_model.ipynb`

## Licences

- **Yahoo Finance** (currency pairs, S&P 500): Yahoo's terms allow personal use but not
  redistribution, so the files are not included. The download code is in `code/01_get_data.ipynb`.
- **FRED** (interest rates, VIX): most series are free to use; the VIX is the property of Cboe
  and is cited as such. For consistency, all data is downloaded by code rather than stored here.
