import pytest

from utils.timer import Timer


@pytest.fixture
def arguments():
    start_time = 0.0
    end_time = 5.0
    return start_time, end_time


def test_press_timer():

    assert Timer().press_timer()


def test_time_remaining(arguments):
    start_time, end_time = arguments

    assert Timer().time_remaining(start_time=start_time, end_time=end_time)
