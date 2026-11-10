"""Shared paths and the project-wide random seed.

Every notebook, script, test and the app imports paths from here, so the
project runs the same way on every laptop.
"""
import os
import random
from pathlib import Path

import numpy as np

SEED = 42

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS = ROOT / "models"
FIGURES = ROOT / "reports" / "figures"
DOCS = ROOT / "docs"


# --- The decision ------------------------------------------------------------
# Owned by the Problem lead. The reasoning behind each value is in
# docs/problem_framing.md; change a value there and here together.

CITY = "Accra"
TIMEZONE = "Africa/Accra"

PM25_THRESHOLD = 35.0
"""µg/m³. The label is 1 when the next day's 24-hour mean PM2.5 is ABOVE this.

The US EPA AQI (2024) puts 35.5 and above in "Unhealthy for Sensitive Groups"
(the "Moderate" band tops out at 35.4). Our approved proposal says "above 35".
"""

HORIZON_DAYS = 1
"""We predict the day after the day the prediction is made (an evening warning)."""

HARMATTAN_MONTHS = (11, 12, 1, 2)
"""November to February: the dry, dusty Harmattan season (Alli et al., 2021)."""

WHO_24H_GUIDELINE = 15.0
"""µg/m³. WHO 2021 guideline for the 24-hour mean. Context only; not our label."""


def set_seed(seed: int = SEED) -> None:
    """Fix every random number generator we use. Call at the top of each notebook.

    Models still need ``random_state=SEED`` passed explicitly.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
