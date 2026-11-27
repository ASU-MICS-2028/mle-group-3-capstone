"""The prediction contract the app depends on."""
from datetime import date

import pandas as pd

from src import config
from src.predict import predict_next_day

D = date(2026, 12, 1)


def days(*values, start="2026-11-29"):
    """One site's daily table, one value per consecutive day."""
    return pd.DataFrame({
        "date": pd.date_range(start, periods=len(values), freq="D").strftime("%Y-%m-%d"),
        "pm25_mean": values,
    })


def test_above_threshold_gives_warning():
    f = predict_next_day(days(20.0, 30.0, 36.0), as_of=D, site="A")
    assert f.status == "warning"
    assert f.latest_pm25 == 36.0
    assert f.site == "A"


def test_below_threshold_gives_safe():
    assert predict_next_day(days(50.0, 50.0, 34.0), as_of=D).status == "safe"


def test_exactly_at_threshold_is_safe():
    """The label is 'above' the threshold, so equal counts as safe."""
    f = predict_next_day(days(1.0, 1.0, config.PM25_THRESHOLD), as_of=D)
    assert f.status == "safe"


def test_predicts_the_next_day():
    f = predict_next_day(days(10.0, 10.0, 10.0), as_of=D)
    assert (f.for_date - f.as_of).days == config.HORIZON_DAYS


def test_missing_reading_today_gives_no_data():
    f = predict_next_day(days(40.0, 40.0, None), as_of=D)
    assert f.status == "no_data"
    assert f.latest_pm25 is None


def test_no_row_for_today_gives_no_data():
    f = predict_next_day(days(40.0, 40.0), as_of=D)  # rows stop the day before
    assert f.status == "no_data"


def test_future_rows_are_ignored():
    """A reading from after the prediction evening must not change the answer."""
    with_future = days(10.0, 10.0, 10.0, 90.0)  # the 90 is 2 Dec, the day we predict
    assert predict_next_day(with_future, as_of=D).status == "safe"


# --- The trained-model path (issue P6), using a stand-in model -----------------
import numpy as np  # noqa: E402

from src.predict import TrainedModel, load_model  # noqa: E402


class FakePipeline:
    """Stands in for a fitted scikit-learn Pipeline: chance = today's PM2.5 / 100."""

    def predict_proba(self, X):
        p = np.clip(X["pm25_today"].to_numpy(dtype=float) / 100, 0, 1)
        return np.column_stack([1 - p, p])


def fake_model(seen=None, threshold=0.4):
    def make_features(rows):
        if seen is not None:
            seen.append(rows["date"].max())
        return pd.DataFrame({"date": rows["date"], "pm25_today": rows["pm25_mean"]})
    return TrainedModel(FakePipeline(), threshold, ["pm25_today"], "Stand-in", make_features)


def test_model_gives_a_probability_and_warning():
    f = predict_next_day(days(10.0, 10.0, 45.0), as_of=D, model=fake_model())
    assert f.status == "warning"
    assert f.probability == 0.45
    assert "Stand-in" in f.method


def test_model_below_its_threshold_is_safe():
    f = predict_next_day(days(10.0, 10.0, 30.0), as_of=D, model=fake_model(threshold=0.4))
    assert f.status == "safe" and f.probability == 0.30


def test_model_never_sees_future_rows():
    seen = []
    predict_next_day(days(10.0, 10.0, 10.0, 90.0), as_of=D, model=fake_model(seen))
    assert seen == ["2026-12-01"]


def test_model_with_missing_reading_today_gives_no_data():
    f = predict_next_day(days(40.0, 40.0, None), as_of=D, model=fake_model())
    assert f.status == "no_data" and f.probability is None


def test_no_saved_model_means_the_rule_is_used():
    # models/ is git-ignored and empty on a fresh clone
    assert load_model() is None
