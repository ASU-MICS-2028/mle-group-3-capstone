# Task split — AirWatch Accra

Roles were drawn at random on 10 Nov 2026. Every member owns one role, and every member must be
able to explain the whole system in the oral defence. The live board with checklists is shared
separately; this file is the record in the repo.

## 1. Roles

| Role | Owner | Owns | Reviews |
|---|---|---|---|
| **Problem lead** | Eric | The decision and its user, cost of errors, the Streamlit app, the plain-language explainer | Ethics lead's work |
| **Data lead** | Clifford | Downloading data, cleaning, daily aggregation, leakage checks, the data note | Modelling lead's work |
| **Modelling lead** | Mubarak | Features, five models + naive baseline, time-based validation, metrics, saved final model | Data lead's work |
| **Ethics & documentation lead** | Kobina | Datasheet, model card, per-site fairness, proxy analysis, regulatory mapping, assembling the IEEE report | Problem lead's work |

**Review rule:** nothing counts as done until the named reviewer has approved the pull request.

## 2. Milestones (from the project brief)

| Date | Milestone | Expected |
|---|---|---|
| Fri 20 Nov | Mid-check | Data in hand, EDA done, baseline model running |
| Fri 4 Dec | Project clinic | Validation, fairness analysis, first full report draft |
| Fri 11 Dec | Code repo due | Repo, report draft, ethics pack, app complete |
| 14–18 Dec | Presentations | Slides, live demo and defence; final report |

## 3. Problem lead tasks (Eric)

| # | Task | Week | Output | Status |
|---|---|---|---|---|
| P1 | Decision context: who decides, when, what action | 10 | `docs/problem_framing.md` | in progress |
| P2 | Cost of errors; agree recall / false-alarm target with Modelling lead | 10–11 | same doc + `src/config.py` | to do |
| P3 | Talk to one real user, if possible | 11 | notes in the doc | to do |
| P4 | Sketch the app screens | 11 | `docs/app_wireframe.md` | first version; justifications to write |
| P5 | Streamlit app with a placeholder model | 12 | `app/app.py`, `src/predict.py` | done (demo data + naive rule) |
| P6 | Connect the real model | 13 | `app/` | to do |
| P7 | Plain-language explainer and limitations | 13 | `docs/` + in the app | to do |
| P8 | Report sections (intro, framing, deployment, limitations) + presentation slots 1 and 5 | 13–15 | report, slides | to do |

Other roles: add your own task table here in the same format.

## 4. Who presents and writes what

| Presentation slot (time) | Report section | Owner |
|---|---|---|
| 1. Problem and decision (2 min) | Introduction, problem framing | Eric |
| 2. Data and features (3 min) | Data, preprocessing | Clifford |
| 3. Models, validation, results (4 min) | Methods, results | Mubarak |
| 4. Ethics, fairness, regulation (3 min) | Ethics and fairness | Kobina |
| 5. The app and limitations (2 min) | Deployment, limitations | Eric |
| 6. Next steps and contributions (1 min) | Conclusion | All |
