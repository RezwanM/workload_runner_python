import numpy as np


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

    def run(self):
        """Runs the workload."""
        pass

    def process_output(self):
        """Process the test output to determine whether the test passed or failed."""
        pass
