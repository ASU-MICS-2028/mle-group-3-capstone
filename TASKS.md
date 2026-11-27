# Task split — AirWatch Accra

Roles were drawn at random on 10 Nov 2026. Every member owns one role, and every member must be
able to explain the whole system in the oral defence. The live board with checklists is shared
separately; this file is the record in the repo.

## 1. Roles

| Role | Owner | Owns | Reviews |
|---|---|---|---|
| **Problem lead** | Eric Elikplim Sunu (@ElikplimSunu) | The decision and its user, cost of errors, the Streamlit app, the plain-language explainer | Ethics lead's work |
| **Data lead** | Clifford Yeboah (@YCliffe21) | Downloading data, cleaning, daily aggregation, leakage checks, the data note | Modelling lead's work |
| **Modelling lead** | Mubarak Tijani (@Xenongt1) | Features, five models + naive baseline, time-based validation, metrics, saved final model | Data lead's work |
| **Ethics & documentation lead** | Kobina | Datasheet, model card, per-site fairness, proxy analysis, regulatory mapping, assembling the IEEE report | Problem lead's work |

**Review rule:** nothing counts as done until the named reviewer has approved the pull request.

## 2. Milestones (from the project brief)

| Date | Milestone | Expected |
|---|---|---|
| Fri 20 Nov | Mid-check | Data in hand, EDA done, baseline model running |
| Fri 4 Dec | Project clinic | Validation, fairness analysis, first full report draft |
| Fri 11 Dec | Code repo due | Repo, report draft, ethics pack, app complete |
| 14–18 Dec | Presentations | Slides, live demo and defence; final report |

## 3. Tasks

Every task is a GitHub issue with steps, a definition of done, and its milestone. The
[Roadmap issue #35](https://github.com/ASU-MICS-2028/mle-group-3-capstone/issues/35) lists them all.

| Code | Owner | Issues |
|---|---|---|
| D1–D7 | Clifford (Data) | #1–#7 |
| M1–M8 | Mubarak (Modelling) | #8–#15 |
| E1–E7 | Kobina (Ethics & documentation) | #16–#22 |
| P1–P8 | Eric (Problem) | #23–#30 |
| A1–A4 | Everyone | #31–#34 |

Open a pull request per task, write `Closes #N` in it, and ask your reviewer.

## 4. Who presents and writes what

| Presentation slot (time) | Report section | Owner |
|---|---|---|
| 1. Problem and decision (2 min) | Introduction, problem framing | Eric |
| 2. Data and features (3 min) | Data, preprocessing | Clifford |
| 3. Models, validation, results (4 min) | Methods, results | Mubarak |
| 4. Ethics, fairness, regulation (3 min) | Ethics and fairness | Kobina |
| 5. The app and limitations (2 min) | Deployment, limitations | Eric |
| 6. Next steps and contributions (1 min) | Conclusion | All |
