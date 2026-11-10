# Data sources

All sources are public and free. No personal data. No permission or ethics approval needed.
Data files are **not committed** (see `.gitignore`); the Data lead's download script will fetch them
into `data/raw/`, and cleaning code writes to `data/processed/`.

| Role | Source | Link | Licence |
|---|---|---|---|
| Primary | sensors.AFRICA Air Quality Archive, Accra (monthly CSV files) | https://www.openafrica.net/dataset/sensorsafrica-airquality-archive-accra | CC-BY |
| Fallback | AirQo air-quality API (free key) | https://airqo.mak.ac.ug/products/api · key: https://analytics.airqo.net | see AirQo terms |
| Weather | Open-Meteo historical weather archive (no key) | https://open-meteo.com/ | CC-BY 4.0 |

## Things to know about the sensors.AFRICA files
- Column codes: **P0 = PM1, P1 = PM10, P2 = PM2.5**. P2 is the one we predict.
- Monthly files vary a lot in size (one month is 3.9 KB, another 76 MB), so some months have very
  few readings. Check completeness before relying on a month.
- Readings come from low-cost sensors, which are less accurate than reference monitors,
  especially in high humidity.

## Rules
- Files in `raw/` stay exactly as downloaded. All cleaning happens in code.
- API keys go in `.env` at the repo root, never in code or notebooks.
