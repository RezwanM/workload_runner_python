import pytest

from utils.args import Args


@pytest.fixture
def arguments():
    workload = "Workload_1"
    iteration = 3
    time = 60
    seed = 123
    return workload, iteration, time, seed


def test_parse_arguments_iteration(arguments):
    workload, iteration, time, seed = arguments

    parser = Args().get_parser()
    args = parser.parse_args(
        [f"--workload={workload}", f"--iteration={iteration}", f"--seed={seed}"]
    )

    assert (args.workload[0], args.iteration, args.seed) == (workload, iteration, seed)


def test_parse_arguments_time(arguments):
    workload, iteration, time, seed = arguments

    parser = Args().get_parser()
    args = parser.parse_args(
        [f"--workload={workload}", f"--time={time}", f"--seed={seed}"]
    )

    assert (args.workload[0], args.time, args.seed) == (workload, time, seed)


def test_is_iter(arguments):
    workload, iteration, time, seed = arguments

    parser = Args().get_parser()
    args = parser.parse_args([f"--workload={workload}", f"--time={time}"])

    assert Args().get_bool_args(args)["is_iter"] == False


def test_is_random(arguments):
    workload, iteration, time, seed = arguments

    parser = Args().get_parser()
    args = parser.parse_args([f"--workload={workload}", f"--seed={seed}"])

    assert Args().get_bool_args(args)["is_random"] == False
