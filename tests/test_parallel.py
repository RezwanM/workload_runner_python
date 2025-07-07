import pytest

from utils.parallel import Parallel


@pytest.fixture
def arguments():
    parallel = Parallel()

    def function_1(x):
        print(x + 2)

    def function_2(y):
        print(y * 3)

    return parallel, function_1, function_2


def test_start_process(arguments):
    parallel, function_1, function_2 = arguments
    functions = [function_1, function_2]
    for func in functions:
        parallel.start_process(func=func(2))

    assert not parallel.process_list == False


def test_wait(arguments):
    parallel, funciton_1, function_2 = arguments
    parallel.wait()

    assert not parallel.process_list == False
