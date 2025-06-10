"""This module contains functions for printing out information on the terminal when running Workload-Runner. 

Typical usage example:

  logger = Logger()
  logger.run_pre_exec(
      wl_list="Workload_1",
      is_iter=True,
      is_random=False,
  )
"""

from datetime import datetime
import hashlib
import inspect
import os
from pathlib import Path
import struct
import time
from typing import Tuple, List

from .paths import Paths


class Logger:
    """Class definition for handling Workload-Runner's logging capabilities.

    Attributes:
        term_size: The horizontal width of user's terminal.
        hash_length: The length of the hash to be used for creating subdirectory names.
        dir_path: The path to Workload-Runner's log directory.
    """

    def __init__(self):
        """Initializes an instance from the Logger class."""
        self.term_size = os.get_terminal_size().columns
        self.hash_length = 16
        self.dir_path = Paths().dir_path

    def make_log_dir(self):
        """Creates the regression log directory for the regression run."""
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)

    def make_log_subdir(self, seed: int) -> str:
        """Creates the regression log subdirectory for the current iteration.

        Args:
            seed: The iteration seed.

        Returns:
            The absolute path to the subdirectory.
        """
        path = str(Path(self.dir_path, self.get_subdir(seed=seed)))
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def touch_log_files(
        self, seed: int, workload: str, current_iter: int
    ) -> Tuple[str, str]:
        """Creates the regression log files (standard output and standard error) for the current iteration.

        Args:
            seed: The iteration seed.
            workload: The workload selected for regression test.
            current_iter: The current iteration ID.

        Returns:
            The absolute paths to the log files.
        """
        subdir_path = str(Path(self.dir_path, self.get_subdir(seed=seed)))
        paths = self.get_filenames(workload=workload, current_iter=current_iter)
        for path in paths:
            open(str(Path(subdir_path, path)), "a", encoding="utf-8").close()
        return str(Path(subdir_path, paths[0])), str(Path(subdir_path, paths[1]))

    def set_color(self, text: str, color: str) -> str:
        """Changes the color of an input text by padding ANSI codes.

        Args:
            text: The input text.
            color: The color of the output text.

        Returns:
            The colored text.
        """
        right_pad = "\x1b[0m"
        if color == "default":
            left_pad = "\x1b[37m"
        elif color == "green":
            left_pad = "\x1b[32m"
        elif color == "red":
            left_pad = "\x1b[31m"
        elif color == "cyan":
            left_pad = "\x1b[36m"
        colored_text = left_pad + text + right_pad
        return colored_text

    def print_separator(self):
        """Prints a separator line."""
        print("#" * self.term_size)

    def print_to_terminal(self, text: str, fancy: bool = False, color: str = "default"):
        """Prints an input text on the terminal (i.e., standard output).

        Args:
            text: The input text.
            fancy: Whether to pad the text with special characters.
            color: The color of the output text.
        """
        char = " "
        if fancy:
            char = "-"
        text = self.set_color(text=text, color=color)
        pad_len = 9
        text_width = len(text) + 4
        print(text.center(text_width).center(self.term_size + pad_len, char))

    def run_pre_exec(self, wl_list: List[str], is_iter: bool, is_random: bool):
        """Runs the pre-execution stage functions.

        Args:
            wl_list: The list of workloads to be run in the regression test.
            is_iter: Whether input iterations are being used instead of runtime.
            is_random: Whether a random seed was used to start the regression test instead of a user-defined seed.
        """
        self.make_log_dir()
        self.print_banner()
        self.print_wl(wl_list)
        self.print_run_config(is_iter=is_iter, is_random=is_random)

    def run_exec(
        self, seed: int, workload: str, current_iter: int
    ) -> Tuple[str, Tuple[str, str]]:
        """Runs the execution stage functions.

        Args:
            seed: An input seed.
            workload: The workload to be run in the regression test.
            current_iter: The current iteration ID.

        Returns:
            The absolute paths to the log subdirectory and the log files.
        """
        subdir_path = self.make_log_subdir(seed=seed)
        log_paths = self.touch_log_files(
            seed=seed, workload=workload, current_iter=current_iter
        )
        return subdir_path, log_paths

    def run_post_exec(
        self, is_pass: bool, log_paths: Tuple[str, str], attribute: str, iter_id: int
    ) -> int:
        """Runs the post-execution stage functions.

        Args:
            is_pass: Whether the test passed.
            log_paths: The absolute paths to the standard output and standard error log files.

        Returns:
            The exit code.
        """
        if is_pass:
            self.print_to_terminal(f"{iter_id} {attribute}: PASSED!", color="green")
            return 1
        else:
            self.print_to_terminal(f"<{iter_id}> {attribute}: FAILED!", color="red")
            if os.path.exists(log_paths[0]):
                self.print_to_terminal(
                    f"Path to output log: {log_paths[0]}", color="red"
                )
            if os.path.exists(log_paths[1]):
                self.print_to_terminal(
                    f"Path to error log: {log_paths[1]}", color="red"
                )
            return 0

    def print_summary(
        self, pass_count: int, task_count: int, total_iter: int, total_time: float
    ):
        """Prints the final summary of the entire regression run.

        Args:
            pass_count: The number of tests that passed.
            total_iter: The total number of iterations run.
            total_time: The total duration of the run.
        """
        self.print_separator()
        self.print_to_terminal("TEST ENDED", color="cyan")
        time.sleep(2)
        self.print_to_terminal(f"Total runtime: {total_time:.2f} seconds")
        time.sleep(2)
        self.print_to_terminal(f"Total iterations: {total_iter}")
        time.sleep(2)
        self.print_to_terminal(f"Total tasks: {task_count}")
        time.sleep(2)
        self.print_to_terminal(f"Passed: {pass_count}")
        time.sleep(2)
        self.print_to_terminal(f"Failed: {task_count-pass_count}")
        self.print_separator()

    def print_banner(self):
        """Prints the banner for Workload-Runner at the beginning of the regression run."""
        self.print_separator()
        self.print_to_terminal(
            "W o r k l o a d - R u n n e r", fancy=True, color="cyan"
        )
        self.print_separator()
        self.print_to_terminal("by Rezwan Matin", fancy=True)
        self.print_to_terminal("Copyright 2025", fancy=True)
        self.print_separator()
        self.print_to_terminal("TEST STARTED", color="cyan")
        time.sleep(2)
        self.print_to_terminal("Now running...")
        time.sleep(2)

    def print_wl(self, wl_list: List[str]):
        """Prints the list of workloads selected for the regression run.

        Args:
            wl_list: The list of workloads.
        """
        for wl in wl_list:
            self.print_to_terminal("> " + wl + " <")
            time.sleep(2)

    def print_run_config(self, is_iter: bool, is_random: bool):
        """Prints the run configuration selected for the regression run.

        Args:
            is_iter: Whether the regression run is based on input iterations.
            is_random: Whether the regression run was initialized using a random seed.
        """
        if is_random:
            self.print_to_terminal("Test started with a random seed")
        else:
            self.print_to_terminal("Test started with a user-defined seed")
        time.sleep(2)
        if is_iter:
            self.print_to_terminal("Test will run based on input iterations")
        else:
            self.print_to_terminal("Test will run based on input runtime")
        time.sleep(2)

    def print_iter(self, current_iter: int, total_iter: int, seed: int):
        """Prints the seed and iteration ID for each iteration.

        Args:
            current_iter: The current iteration ID.
            total_iter: The total number of iterations to be run.
            seed: The iteration seed.
        """
        self.print_separator()
        self.print_to_terminal(f"Seed: {seed}")
        self.print_to_terminal(f"Iteration {current_iter} of {total_iter}")

    def print_time(self, time_left: float, total_time: float, seed: int):
        """Prints the seed and remaining runtime for each iteration.

        Args:
            time_left: The time remaining till runtime ends.
            total_time: The total runtime.
            seed: The iteration seed.
        """
        left_pad = "\x1b[31m"
        right_pad = "\x1b[0m"
        self.print_separator()
        self.print_to_terminal(f"Seed: {seed}")
        if time_left < 0:
            self.print_to_terminal(
                f"Time remaining: {left_pad}{time_left:.2f}{right_pad} of {total_time} seconds"
            )
        else:
            self.print_to_terminal(
                f"Time remaining: {time_left:.2f} of {total_time} seconds"
            )

    def print_error(self, text: str):
        """Prints an error message on the terminal (i.e., standard output)."""
        self.print_to_terminal(text=text.upper(), color="red")

    def print_debug(self, text: str):
        """Prints a debug message on the terminal (i.e., standard output)."""
        module_name = inspect.stack()[1].filename
        line_number = inspect.stack()[1].lineno
        self.print_to_terminal(
            text=f"Debug: {text}    File: {module_name}    Line: {line_number}",
            color="red",
        )

    def get_subdir(self, seed: int) -> str:
        """Gets the name of the log subdirectory for the current iteration.

        Args:
            seed: The iteration seed.

        Returns:
            The name of the log subdirectory.
        """
        seed_in_bytes = struct.pack(">H", seed)
        hash_object = hashlib.sha256(seed_in_bytes)
        subdir_name = hash_object.hexdigest()[: self.hash_length]
        return subdir_name

    def get_filenames(self, workload: str, current_iter: int) -> Tuple[str, str]:
        """Gets the name of the log files (standard output and standard error) for the current iteration.

        Args:
            workload: The workload for which to create the log files.
            curren_iter: The current iteration ID.

        Returns:
            The name of the log files.
        """
        stdout_name = (
            workload.lower()
            + "_"
            + str(current_iter)
            + "_"
            + datetime.now().strftime("%m%d%Y_%H%M%S")
            + ".out"
        )
        stderr_name = (
            workload.lower()
            + "_"
            + str(current_iter)
            + "_"
            + datetime.now().strftime("%m%d%Y_%H%M%S")
            + ".err"
        )
        return stdout_name, stderr_name
