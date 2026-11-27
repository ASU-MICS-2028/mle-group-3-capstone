# AirWatch Accra

Next-day unhealthy-air warnings for Accra neighbourhoods, built with classical machine learning.

**Course:** ICS553 Machine Learning Essentials, Ashesi University, Fall 2026 (Final Capstone Project)
**Group 3:** Eric Elikplim Sunu (Problem lead) · Clifford Yeboah (Data lead) · Mubarak Tijani (Modelling lead) · Kobina (Ethics & documentation lead)
**Status:** see the [Roadmap issue](https://github.com/ASU-MICS-2028/mle-group-3-capstone/issues/35) for every task, owner and deadline.

## The problem in one sentence
Each evening, predict whether tomorrow's average PM2.5 at an Accra sensor site will go above
35 µg/m³ ("unhealthy for sensitive groups"), so a school head or district health officer can decide
whether to move outdoor activities indoors.

## How the pieces fit together

Who hands what to whom. Numbers are GitHub issues; the [Roadmap (#35)](https://github.com/ASU-MICS-2028/mle-group-3-capstone/issues/35) lists all 34, and the team board has an interactive map of every task.

**Critical path** (any delay here delays everything): #1 → #2 → #8 → #9 → #11 → #12 → #13 → #28.

```mermaid
flowchart TB
  subgraph E["Eric · Problem lead"]
    P1["Decision, threshold,<br/>cut-off time (#23)"]
    P2["Cost matrix +<br/>recall target (#24)"]
    APP["App + user guide<br/>(#27 #28 #29)"]
  end
  subgraph C["Clifford · Data lead"]
    D1["Download + check<br/>(#1)"] --> D2["Clean → daily_pm25.csv<br/>(#2)"]
    D3["Weather (#3)"]
  end
  subgraph M["Mubarak · Modelling lead"]
    M1["Label + time split<br/>(#8)"] --> M4["Baselines + 5 models<br/>(#9 #10 #11)"] --> M5["Validation (#12)"] --> M6["Final model<br/>+ threshold (#13)"]
  end
  subgraph K["Kobina · Ethics & docs lead"]
    E1["Datasheet,<br/>coverage (#16 #17)"]
    E3["Fairness by site,<br/>model card (#18 #21)"]
  end
  R["Everyone: report, slides,<br/>final review (#31–#34)"]
  P1 -- "cut-off time" --> D2
  D2 -- "daily_pm25.csv" --> M1
  D3 -- "weather" --> M4
  P2 -- "recall target" --> M6
  M6 -- "final_model.joblib" --> APP
  D1 -- "data facts" --> E1
  M5 -- "results per site" --> E3
  APP --> R
  E3 --> R
  M6 --> R
  classDef eric stroke:#0d7d8c,stroke-width:2px
  classDef cliff stroke:#a86a12,stroke-width:2px
  classDef mub stroke:#6447d1,stroke-width:2px
  classDef kob stroke:#bb3c66,stroke-width:2px
  class P1,P2,APP eric
  class D1,D2,D3 cliff
  class M1,M4,M5,M6 mub
  class E1,E3 kob
```

## Layout
| Path | What goes in it |
|---|---|
| `src/` | Reusable Python modules, one job each (`config.py`, then data loading, features, models, validation). |
| `notebooks/` | Numbered notebooks (`01_…`, `02_…`) that import from `src/` and run top to bottom. |
| `tests/` | Automatic checks for `src/` (run with `python -m pytest -q`). |
| `app/` | The Streamlit app people actually use. |
| `docs/` | Problem framing, datasheet, model card, app explainer. |
| `reports/` | Report, result tables (CSV) and `figures/`. |
| `scripts/` | Command-line helpers (download data, run everything). |
| `data/` | Not committed. `data/README.md` says where each file comes from. |
| `models/` | Not committed. Saved trained models. |

## Setup
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest -q            # check everything works
```

## How to reproduce (to be completed)
1. Download the data: *(script to come, `scripts/`)*
2. Build the dataset, train, evaluate: *(to come)*
3. Run the app: `streamlit run app/app.py`

## Conventions
- Constants (paths, seed, the 35 µg/m³ threshold) come from `src/config.py`, never hard-coded.
- Split by time, never at random. Preprocessing is fitted on training data only.
- Work on a branch (`problem/…`, `data/…`, `modelling/…`, `ethics/…`) and open a pull request;
  the reviewer in `TASKS.md` approves it.
- Keep personal notes in `personal/` (ignored by Git).

## Who does what
Roles and reviewers: `TASKS.md`. Every task is a GitHub issue, grouped by milestone in the
[Roadmap issue](https://github.com/ASU-MICS-2028/mle-group-3-capstone/issues/35).
