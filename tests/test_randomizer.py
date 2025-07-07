import numpy as np
import pytest

from utils.randomizer import Randomizer


@pytest.fixture
def arguments():
    low = 100
    high = 999
    seed = 123
    return low, high, seed


def test_generate_seed(arguments):
    low, high, seed = arguments
    seed = np.random.choice(a=range(low, high), replace=False)

    assert seed


def test_generate_seed_from_seed(arguments):
    low, high, seed = arguments
    rng = np.random.default_rng(seed=seed)
    number = rng.integers(low=low, high=high, size=1)

    assert Randomizer().generate_seed_from_seed(seed=seed) == number[0]


def test_pick_random_int(arguments):
    low, high, seed = arguments
    rng = np.random.default_rng(seed=seed)
    number = rng.integers(low=low, high=high, size=1)

    assert Randomizer().pick_random_int(low=low, high=high, seed=seed) == number[0]
