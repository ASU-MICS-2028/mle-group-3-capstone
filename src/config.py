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


def set_seed(seed: int = SEED) -> None:
    """Fix every random number generator we use. Call at the top of each notebook.

    Models still need ``random_state=SEED`` passed explicitly.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
