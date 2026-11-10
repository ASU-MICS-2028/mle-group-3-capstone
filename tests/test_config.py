"""The shared config points at the real repo and makes randomness repeatable."""
import numpy as np

from src import config


def test_root_is_the_repo():
    assert (config.ROOT / "README.md").exists()
    assert (config.ROOT / "src" / "config.py").exists()


def test_set_seed_repeats_random_numbers():
    config.set_seed()
    first = np.random.rand(3)
    config.set_seed()
    assert np.allclose(first, np.random.rand(3))
