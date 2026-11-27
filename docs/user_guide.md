# AirWatch Accra: user guide

Owner: Eric (Problem lead) · Reviewer: Kobina · Status: **draft** (how-to steps written;
limitations to be finalised in Eric's own words)

AirWatch Accra tells a school, each evening, whether tomorrow's air near its nearest sensor is
likely to be unhealthy for children with asthma and other sensitive groups.

## 1. Start the app (one-time setup, about 10 minutes)

You need Python 3.10 or newer.

```bash
git clone https://github.com/ASU-MICS-2028/mle-group-3-capstone.git
cd mle-group-3-capstone
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app/app.py
```

A browser tab opens at http://localhost:8501. To start it again later, run the last line from
the same folder (after `source .venv/bin/activate`).

## 2. Read the screen

1. **Choose the sensor nearest your school** from the list.
2. Read the coloured card. It is about **tomorrow**, with the date at the top:

| Card | What it means | Suggested action |
|---|---|---|
| **Warning: unhealthy air likely** (orange) | Tomorrow's average PM2.5 is expected to go above 35 µg/m³ | Move PE, sports and assemblies indoors; let parents of children with asthma know |
| **Likely safe** (green) | Tomorrow is expected to stay at or below 35 µg/m³ | Carry on as normal |
| **No prediction today** (grey) | The sensor sent no reading today, so we don't guess | Use your usual judgement; check again tomorrow evening |

3. **How we worked this out** shows today's level, the method used, and (once the trained model is
   in use) the chance of unhealthy air. The chart shows the last 14 days against the 35 line.
4. If you see a yellow **Demo mode** banner, the numbers are made up for testing. Don't act on them.

## 3. When to check
[YOUR WORDS: the time each evening the prediction is ready, from the cut-off decided in
`docs/problem_framing.md`.]

## 4. Limitations: please read
- **Advice only.** This is not an official Ghana EPA alert. [YOUR WORDS: one line on how it sits
  beside official information.]
- **Low-cost sensors.** Readings can be off, especially in very humid weather.
- **Not every area has a sensor.** [YOUR WORDS: point to the coverage findings (issue E2) and say
  what a school far from any sensor should do.]
- **One day ahead only.** It does not forecast further.
- **It will sometimes be wrong.** [YOUR WORDS: in plain terms, how often it misses a bad day and
  how often it gives a false alarm, using the final test results (issue M6).]

## AI-use declaration
[YOUR WORDS]
