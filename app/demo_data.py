"""Made-up daily PM2.5 values for testing the app's screens.

NOT real readings. The app shows a banner whenever it uses these, and stops
using them as soon as the Data lead's cleaned file exists.
"""
from datetime import date

import numpy as np
import pandas as pd

from src import config

# (site name, typical level in µg/m³, show a missing reading on the last day?)
DEMO_SITES = (
    ("Demo site A", 26.0, False),
    ("Demo site B", 44.0, False),
    ("Demo site C", 30.0, True),
)


def make_demo_daily(end: date, n_days: int = 30, seed: int = config.SEED) -> pd.DataFrame:
    """A table in the same shape as ``config.DAILY_PM25_FILE``, ending on ``end``."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(end=pd.Timestamp(end), periods=n_days, freq="D")
    rows = []
    for site, level, gap_today in DEMO_SITES:
        wobble = np.cumsum(rng.normal(0, 3, n_days))  # slow drift up and down
        values = np.clip(level + wobble - wobble.mean() + rng.normal(0, 4, n_days), 5, None)
        values = values.round(1).astype(object)
        if gap_today:
            values[-1] = None
        rows += [
            {"site": site, "date": d.strftime("%Y-%m-%d"), "pm25_mean": v}
            for d, v in zip(dates, values)
        ]
    return pd.DataFrame(rows, columns=list(config.DAILY_COLUMNS))
