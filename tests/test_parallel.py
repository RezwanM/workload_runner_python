import pytest

from utils.parallel import Parallel


@pytest.fixture
def arguments():
    function_1 = lambda x: x + 2
    function_2 = lambda y: y * 3
    return function_1, function_2


def test_process_list(arguments):
    functions = arguments
    for func in functions:
        Parallel().start_process(func(2))

    assert not Parallel().process_list == False
