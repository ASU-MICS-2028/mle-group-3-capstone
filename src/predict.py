"""Tomorrow's air-quality warning for one sensor site.

This is the one function the app calls. Today it uses the naive baseline
"tomorrow will be like today". When the Modelling lead's trained model is
ready, it replaces the rule inside ``predict_next_day``; the app, which only
sees the ``Forecast`` it returns, does not change.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Literal, Optional

import pandas as pd

from src import config

Status = Literal["warning", "safe", "no_data"]

BASELINE_METHOD = "Simple rule: tomorrow will be like today"


@dataclass(frozen=True)
class Forecast:
    """What the app shows for one site."""

    site: str
    as_of: date              # the evening the prediction is made (day D)
    for_date: date           # the day being predicted (D + horizon)
    status: Status           # "warning", "safe", or "no_data"
    latest_pm25: Optional[float]  # day D's mean PM2.5, µg/m³
    probability: Optional[float]  # chance tomorrow is unhealthy; None for the rule
    method: str              # how the prediction was made, in plain words


def predict_next_day(daily: pd.DataFrame, as_of: date, site: str = "") -> Forecast:
    """Predict whether ``site`` will be above the threshold the day after ``as_of``.

    ``daily`` holds one site's rows with columns ``date`` and ``pm25_mean``
    (see ``config.DAILY_COLUMNS``). Rows after ``as_of`` are ignored, so the
    prediction can never use information from the future.
    """
    for_date = as_of + timedelta(days=config.HORIZON_DAYS)
    dates = pd.to_datetime(daily["date"]).dt.date
    known = daily.loc[dates <= as_of].assign(_d=dates[dates <= as_of])

    today = known.loc[known["_d"] == as_of, "pm25_mean"].dropna()
    if today.empty:
        return Forecast(site, as_of, for_date, "no_data", None, None, BASELINE_METHOD)

    latest = float(today.iloc[-1])
    status: Status = "warning" if latest > config.PM25_THRESHOLD else "safe"
    return Forecast(site, as_of, for_date, status, latest, None, BASELINE_METHOD)
