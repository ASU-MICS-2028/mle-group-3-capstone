"""AirWatch Accra: tomorrow's air-quality warning for a school.

Run from the repo root:  streamlit run app/app.py
"""
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))  # so `src` imports work when Streamlit runs this file

import altair as alt  # noqa: E402  (ships with Streamlit)
import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

from app.demo_data import make_demo_daily  # noqa: E402
from src import config  # noqa: E402
from src.predict import Forecast, load_model, predict_next_day  # noqa: E402

# Draft wording: Eric to confirm in docs/problem_framing.md (tasks P1 and P3).
ADVICE = {
    "warning": "Move PE, sports and assemblies indoors tomorrow. Let parents of children "
               "with asthma know.",
    "safe": "Outdoor activities can go ahead as normal tomorrow.",
    "no_data": "This sensor has no reading for today, so we can't make a prediction. "
               "Use your usual judgement, and check again tomorrow evening.",
}
HEADLINE = {"warning": "Warning: unhealthy air likely", "safe": "Likely safe",
            "no_data": "No prediction today"}
COLOURS = {"warning": "#c2410c", "safe": "#15803d", "no_data": "#6b7280"}


@st.cache_data
def load_daily() -> tuple[pd.DataFrame, bool]:
    """The cleaned daily table if it exists, otherwise demo data. Returns (table, is_demo)."""
    if config.DAILY_PM25_FILE.exists():
        df = pd.read_csv(config.DAILY_PM25_FILE)
        return df[list(config.DAILY_COLUMNS)], False
    return make_demo_daily(end=date.today()), True


@st.cache_resource
def get_model():
    """The Modelling lead's saved model, or None (then the simple rule is used)."""
    return load_model()


def nice_date(d: date) -> str:
    return f"{d:%A} {d.day} {d:%B}"


def status_card(f: Forecast) -> None:
    colour = COLOURS[f.status]
    st.markdown(
        f"""<div style="border-left: 8px solid {colour}; padding: 1rem 1.25rem;
        border-radius: 8px; background: {colour}14; margin-bottom: 0.5rem;">
        <div style="font-size: 0.9rem; opacity: 0.8;">{nice_date(f.for_date)} · {f.site}</div>
        <div style="font-size: 1.8rem; font-weight: 700; color: {colour};">{HEADLINE[f.status]}</div>
        <div style="font-size: 1.05rem; margin-top: 0.4rem;">{ADVICE[f.status]}</div></div>""",
        unsafe_allow_html=True,
    )


def history_chart(site_rows: pd.DataFrame, as_of: date) -> alt.Chart:
    data = site_rows.assign(date=pd.to_datetime(site_rows["date"]))
    data = data[data["date"] <= pd.Timestamp(as_of)].tail(14)
    top = max(config.PM25_THRESHOLD * 1.4, float(data["pm25_mean"].max(skipna=True) or 0) * 1.1)
    line = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X("date:T", title=None, axis=alt.Axis(format="%d %b")),
        y=alt.Y("pm25_mean:Q", title="Daily average PM2.5 (µg/m³)",
                scale=alt.Scale(domain=[0, top])),
        tooltip=[alt.Tooltip("date:T", format="%a %d %b"), alt.Tooltip("pm25_mean:Q", format=".1f")],
    )
    rule = alt.Chart(pd.DataFrame({"y": [config.PM25_THRESHOLD]})).mark_rule(
        strokeDash=[6, 4], color=COLOURS["warning"]).encode(y="y:Q")
    label = alt.Chart(pd.DataFrame({"y": [config.PM25_THRESHOLD],
                                    "t": [f"Warning line: {config.PM25_THRESHOLD:g}"]})).mark_text(
        align="left", dx=4, dy=-8, color=COLOURS["warning"]).encode(y="y:Q", text="t:N", x=alt.value(0))
    return (line + rule + label).properties(height=280)


def main() -> None:
    st.set_page_config(page_title="AirWatch Accra", page_icon="🌫️", layout="centered")
    st.title("AirWatch Accra")
    st.caption("Tomorrow's air quality at your nearest sensor, for school decisions.")

    daily, is_demo = load_daily()
    if is_demo:
        st.warning("**Demo mode.** These are made-up numbers for testing the screens, "
                   "not real readings. Real Accra sensor data will replace them.")

    sites = sorted(daily["site"].dropna().unique())
    site = st.selectbox("Choose the sensor nearest your school", sites)
    site_rows = daily[daily["site"] == site].sort_values("date")
    as_of = pd.to_datetime(daily["date"]).max().date()

    f = predict_next_day(site_rows, as_of=as_of, site=site, model=get_model())
    status_card(f)

    st.subheader("How we worked this out")
    if f.latest_pm25 is not None:
        st.write(f"Today's average at this sensor was **{f.latest_pm25:.1f} µg/m³**. "
                 f"We warn when we expect tomorrow to go above **{config.PM25_THRESHOLD:g} µg/m³**, "
                 "the level where air becomes unhealthy for sensitive groups such as children "
                 "with asthma.")
    if f.probability is not None:
        st.metric("Chance of unhealthy air tomorrow", f"{f.probability:.0%}")
    st.write(f"Method: {f.method}.")
    st.altair_chart(history_chart(site_rows, as_of), width="stretch")

    with st.expander("What do these words mean?"):
        st.markdown(
            "- **PM2.5**: tiny bits of dust and smoke, small enough to reach deep into the lungs.\n"
            "- **µg/m³**: micrograms per cubic metre, how much of it is in the air.\n"
            "- **Harmattan**: the dry, dusty season (November to February), when levels are "
            "usually much higher."
        )
    st.caption("Advice only, not an official Ghana EPA alert. Low-cost sensors can be "
               "inaccurate, especially in very humid weather.")


main()
