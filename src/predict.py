"""Tomorrow's air-quality warning for one sensor site.

This is the one function the app calls. It has two ways to answer:

* **Trained model** (when ``models/final_model.joblib`` and ``.json`` exist):
  the model gives the chance that tomorrow is unhealthy, and we warn when
  that chance reaches the threshold chosen on validation data.
* **Simple rule** (until then): tomorrow will be like today.

The app only sees the ``Forecast`` returned, so swapping one for the other
never changes the app.

Saved-model contract (Modelling lead, issue M6):
  models/final_model.joblib  a fitted scikit-learn Pipeline with predict_proba
  models/final_model.json    {"name": str, "threshold": float, "features": [str, ...],
                              "trained_on": str}
Features come from ``src.features.make_features(daily, weather)`` (issue M3),
which returns one row per site-day, built only from data up to that day.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any, Callable, Literal, Optional

import pandas as pd

from src import config

Status = Literal["warning", "safe", "no_data"]

BASELINE_METHOD = "Simple rule: tomorrow will be like today"
MODEL_FILE = config.MODELS / "final_model.joblib"
MODEL_META = config.MODELS / "final_model.json"
WEATHER_FILE = config.DATA_PROCESSED / "weather_daily.csv"


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


@dataclass(frozen=True)
class TrainedModel:
    """A saved model plus what's needed to use it."""

    pipeline: Any                                     # anything with predict_proba
    threshold: float                                  # warn when chance >= this
    features: list                                    # column names the pipeline expects
    name: str                                         # e.g. "Random forest"
    make_features: Callable[[pd.DataFrame], pd.DataFrame]  # site rows -> feature rows

    @property
    def method(self) -> str:
        return f"Trained model ({self.name}), warning when the chance is {self.threshold:.0%} or more"


def load_model() -> Optional[TrainedModel]:
    """The saved final model, or None if the Modelling lead hasn't saved one yet."""
    if not (MODEL_FILE.exists() and MODEL_META.exists()):
        return None
    import joblib

    from src.features import make_features  # written in issue M3

    meta = json.loads(MODEL_META.read_text())
    weather = pd.read_csv(WEATHER_FILE) if WEATHER_FILE.exists() else None
    return TrainedModel(
        pipeline=joblib.load(MODEL_FILE),
        threshold=float(meta["threshold"]),
        features=list(meta["features"]),
        name=str(meta.get("name", "trained model")),
        make_features=lambda rows: make_features(rows, weather),
    )


def predict_next_day(daily: pd.DataFrame, as_of: date, site: str = "",
                     model: Optional[TrainedModel] = None) -> Forecast:
    """Predict whether ``site`` will be above the threshold the day after ``as_of``.

    ``daily`` holds one site's rows with columns ``site``, ``date`` and
    ``pm25_mean`` (see ``config.DAILY_COLUMNS``). Rows after ``as_of`` are
    dropped first, so neither the rule nor the model can see the future.
    With no reading for ``as_of`` we return "no_data" rather than guess.
    """
    for_date = as_of + timedelta(days=config.HORIZON_DAYS)
    dates = pd.to_datetime(daily["date"]).dt.date
    known = daily.loc[dates <= as_of]
    known_dates = dates[dates <= as_of]

    today = known.loc[known_dates == as_of, "pm25_mean"].dropna()
    if today.empty:
        method = model.method if model else BASELINE_METHOD
        return Forecast(site, as_of, for_date, "no_data", None, None, method)
    latest = float(today.iloc[-1])

    if model is None:
        status: Status = "warning" if latest > config.PM25_THRESHOLD else "safe"
        return Forecast(site, as_of, for_date, status, latest, None, BASELINE_METHOD)

    feats = model.make_features(known)
    feat_dates = pd.to_datetime(feats["date"]).dt.date
    row = feats.loc[feat_dates == as_of, model.features]
    if row.empty or row.isna().all(axis=None):
        return Forecast(site, as_of, for_date, "no_data", latest, None, model.method)
    chance = float(model.pipeline.predict_proba(row.tail(1))[0, 1])
    status = "warning" if chance >= model.threshold else "safe"
    return Forecast(site, as_of, for_date, status, latest, chance, model.method)
