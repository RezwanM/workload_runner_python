import os
import pytest

from utils.paths import Paths


@pytest.fixture
def arguments():
    workload = "Workload_1"
    return workload


def test_project_root():

    assert os.path.exists(Paths().project_root)


def test_wl_path():

    assert os.path.exists(Paths().wl_path)


def test_bins_path():

    assert os.path.exists(Paths().bins_path)


def test_dir_path():

    assert os.path.exists(Paths().dir_path)


def test_wl_module(arguments):
    workload = arguments
    mod_string = f"workloads.{workload}.{workload}".lower()

    assert Paths().get_wl_module(workload) == mod_string


def test_wl_config(arguments):
    workload = arguments
    mod_string = f"workloads.{workload}.run_config".lower()

    assert Paths().get_wl_config(workload) == mod_string
