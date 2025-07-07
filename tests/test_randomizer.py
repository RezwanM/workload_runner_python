import pytest

from utils.randomizer import Randomizer


@pytest.fixture
def arguments():
    low = 100
    high = 999
    seed = 123
    return low, high, seed


def test_generate_seed(arguments):

    assert Randomizer().generate_seed()


def test_generate_seed_from_seed(arguments):
    low, high, seed = arguments

    assert Randomizer().generate_seed_from_seed(seed=seed)


def test_pick_random_int(arguments):
    low, high, seed = arguments

    assert Randomizer().pick_random_int(low=low, high=high, seed=seed)
