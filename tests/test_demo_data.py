"""Demo data has the agreed shape, so the app works the same with real data."""
from datetime import date

from app.demo_data import make_demo_daily
from src import config


def test_demo_data_matches_the_daily_file_shape():
    df = make_demo_daily(end=date(2026, 12, 1), n_days=10)
    assert tuple(df.columns) == config.DAILY_COLUMNS
    assert df["date"].max() == "2026-12-01"
    assert df.groupby("site").size().eq(10).all()


def test_demo_data_is_repeatable():
    a = make_demo_daily(end=date(2026, 12, 1))
    b = make_demo_daily(end=date(2026, 12, 1))
    assert a.equals(b)
