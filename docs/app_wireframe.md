# App wireframe — AirWatch Accra (task P4)

Owner: Eric (Problem lead) · Reviewer: Kobina · Status: **first version built** (`app/app.py`,
running on demo data and the naive rule)

## The one screen

```
┌──────────────────────────────────────────────────────────┐
│ AirWatch Accra                                           │
│ Tomorrow's air quality at your nearest sensor            │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ ⚠ Demo mode: made-up numbers (only until real data)  │ │
│ └──────────────────────────────────────────────────────┘ │
│ Choose the sensor nearest your school   [ Site ▾ ]       │
│ ┃ Saturday 28 November · Site                          │ │
│ ┃ WARNING: UNHEALTHY AIR LIKELY   (or LIKELY SAFE /    │ │
│ ┃                                  NO PREDICTION TODAY)│ │
│ ┃ What to do tomorrow, in one sentence                 │ │
│ How we worked this out                                   │
│   Today's average: 41.2 µg/m³ · warning line: 35         │
│   Method: simple rule (later: the trained model + chance)│
│   [ 14-day line chart with dashed 35 line ]              │
│ ▸ What do these words mean?                              │
│ Advice only, not an official Ghana EPA alert.            │
└──────────────────────────────────────────────────────────┘
```

## How it connects

`app/app.py` → `src/predict.py` (`predict_next_day`) → today the naive rule; later the
Modelling lead's saved model. The app reads `config.DAILY_PM25_FILE` (written by the Data
lead's code) and falls back to labelled demo data until that file exists.

## Design choices to justify in the report

| Choice | Built as | Why |
|---|---|---|
| Three states, not two | Warning / Likely safe / No prediction | [YOUR WORDS: why never guess when today's reading is missing?] |
| Advice sentence under the headline | One action per state | [YOUR WORDS: why tell the user what to do, not just a number?] |
| "How sure" | Shown once the model gives a probability | [YOUR WORDS] |
| Plain-language glossary | Folded away by default | [YOUR WORDS] |
| "Advice only" footer | Always shown | [YOUR WORDS: link to limitations and the EPA's role] |

## Still to do
- Confirm the advice wording with a real teacher or school head (task P3).
- Show the model's probability ("how sure") once the Modelling lead's model is ready (task P6).
