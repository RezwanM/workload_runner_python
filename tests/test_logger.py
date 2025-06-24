import os
import pytest
import shutil

from utils.logger import Logger


@pytest.fixture
def arguments():
    workload = "Workload_1"
    iteration = 3
    time = 60
    seed = 123
    return workload, iteration, time, seed

def test_log_dir(tmp_path):
    if os.path.exists(Logger().dir_path):
        shutil.rmtree(Logger().dir_path)
    new_dir = tmp_path / Logger().dir_path
    new_dir.mkdir()

    assert new_dir.exists()

def test_log_subdir(arguments, tmp_path):
    workload, iteration, time, seed = arguments
    if os.path.exists(Logger().dir_path + Logger().get_subdir(seed=seed)):
        shutil.rmtree(Logger().dir_path + Logger().get_subdir(seed=seed))
    sub_dir = tmp_path / (Logger().dir_path + Logger().get_subdir(seed=seed))
    sub_dir.mkdir()

    assert sub_dir.exists()

def test_std_out(arguments, tmp_path):
    workload, iteration, time, seed = arguments
    if os.path.exists(Logger().dir_path + Logger().get_subdir(seed=seed) + Logger().get_filenames(workload=workload, current_iter=iteration)[0]):
        os.remove(Logger().dir_path + Logger().get_subdir(seed=seed) + Logger().get_filenames(workload=workload, current_iter=iteration)[0])
    std_out = tmp_path / (Logger().dir_path + Logger().get_subdir(seed=seed) + Logger().get_filenames(workload=workload, current_iter=iteration)[0])
    std_out.write_text("Test output log message!")

    assert std_out.read_text() == "Test output log message!"

def test_std_err(arguments, tmp_path):
    workload, iteration, time, seed = arguments
    if os.path.exists(Logger().dir_path + Logger().get_subdir(seed=seed) + Logger().get_filenames(workload=workload, current_iter=iteration)[0]):
        os.remove(Logger().dir_path + Logger().get_subdir(seed=seed) + Logger().get_filenames(workload=workload, current_iter=iteration)[0])
    std_err = tmp_path / (Logger().dir_path + Logger().get_subdir(seed=seed) + Logger().get_filenames(workload=workload, current_iter=iteration)[0])
    std_err.write_text("Test output error message!")

    assert std_err.read_text() == "Test output error message!"
