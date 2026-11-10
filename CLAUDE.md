# AirWatch Accra — ICS553 final capstone (Group 3)

Team instructions for Claude Code in this repo. Personal preferences go in your own
`CLAUDE.local.md` (git-ignored), not here.

## What we are building
- **Task:** binary classification. Label = 1 if the next day's 24-hour mean PM2.5 at a sensor site
  is above 35 µg/m³ (`src/config.py` holds the exact value), else 0.
- **User and decision:** a school head or district environmental health officer deciding each
  evening whether to move outdoor activities indoors or issue a warning.
- **Worst error:** a false negative (missed bad-air day). Prioritise recall; keep precision usable.
- **Models:** classical only (logistic regression, decision tree, random forest, gradient boosting,
  SVM) plus a naive "tomorrow = today" baseline. No deep learning (lecturer's rule).
- **Artefact:** a Streamlit app in `app/`.
- **Data:** see `data/README.md`. Scope is Greater Accra; Lagos is a stretch goal only.

## Roles
Problem lead: Eric · Data lead: Clifford · Modelling lead: Mubarak · Ethics & documentation lead: Kobina.

## Code layout
- Reusable logic lives in `src/` as small modules (one job each). Notebooks import from `src/`;
  they do not define functions the app or tests need.
- Constants (paths, seed, the decision threshold) live in `src/config.py`. Never hard-code them.
- Notebooks are numbered `NN_topic.ipynb` and must run top to bottom from a fresh kernel.
- Every function in `src/` that other code relies on has a test in `tests/`.

## Hard rules
- **Split by time, never randomly.** Train on earlier dates, test on later ones.
- **Fit preprocessing on training data only** (scalers, imputers, thresholds): use scikit-learn Pipelines.
- **No future information in features.** A feature for day D uses only data up to the end of day D.
- **Never invent numbers or references.** Every figure cites the notebook or script that produced it.
- Files in `data/raw/` are never edited. API keys go in `.env`, never in code.
- **Submitted writing must be in the students' own voice** (lecturer's AI policy). Draft skeletons
  and code; mark where a student's own words must go with `[YOUR WORDS: ...]`. Every deliverable
  ends with an AI-use declaration.
- Never commit anything under `personal/` or `CLAUDE.local.md`.

## Git
- `main` is the shared branch. Work on a branch named `<area>/<short-topic>`
  (e.g. `problem/framing`, `data/download`, `modelling/baselines`) and open a pull request.
- The reviewer named in `TASKS.md` approves before merging.
- British spelling in docs. Short commit messages that say what changed and why.
