"""This module contains functions for Workload_1.

Typical usage example:

  wl = Workload()
  wl.run(
      seed=123,
      bin_path=".../bins/workload_1/wl_1.sh",
      stdout_path=".../var/log/workload_runner/302cca50069bbc56/workload_1_1_04102025_141638.out",
      stderr_path=".../var/log/workload_runner/302cca50069bbc56/workload_1_1_04102025_141638.err",
  )
"""

import numpy as np
import subprocess


class Workload:
    """Class definition for handling the workload's functions."""

    def __init__(self):
        """Initializes an instance from the Workload class."""
        pass

    def generate_random(self, low: int, high: int, seed: int) -> int:
        """Picks a random integer from a range of integers.

        Args:
            low: The lowest integer in the range.
            high: The highest integer in the range.
            seed: The input seed for the bit generator.

        Returns:
            The random integer.
        """
        rng = np.random.default_rng(seed=seed)
        self.number = rng.integers(low=low, high=high, size=1)
        return self.number[0]

    def run(self, seed: int, bin_path: str, stdout_path: str, stderr_path: str):
        """Runs the workload.

        Args:
            seed: The input seed for the bit generator.
            bin_path: The absolute path to the workload's executable.
            stdout_path: The absolute path to the stdout log file.
            stderr_path: The absolute path to the stderr log file.

        Returns:
            The random integer.
        """
        self.num = str(self.generate_random(low=0, high=100, seed=seed))
        with open(stdout_path, "a") as stdout_file, open(
            stderr_path, "a"
        ) as stderr_file:
            subprocess.run(
                ["sh", bin_path, "-n", self.num], stdout=stdout_file, stderr=stderr_file
            )

    def process_output(self, stdout_path: str) -> bool:
        """Process the test output to determine whether the test passed or failed.

        Args:
            stdout_path: The absolute path to the stdout log file.

        Returns:
            Whether the test passed or failed.
        """
        regex_pattern = "The number picked is :"
        with open(stdout_path, "r") as stdout_file:
            content = stdout_file.read()
        if regex_pattern not in content:
            return False
        return True
