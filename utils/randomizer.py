"""This module contains functions related to random selections in Workload-Runner. 

Typical usage example:

  randomizer = Randomizer()
  start_seed = randomizer.generate_seed()
  random_number = randomizer.pick_random_int(
                      low=0, high=len(wl_config[wl].attributes), seed=current_seed
                  )
"""

import numpy as np


class Randomizer:
    """Class definition for handling Workload-Runner's random selections.

    Attributes:
        low: The lowest integer in a range from which to pick a seed.
        high: The highest integer in a range from which to pick a seed.
    """

    def __init__(self):
        """Initializes an instance from the Randomizer class."""
        self.low = 100
        self.high = 999

    def generate_seed(self) -> int:
        """Generates a random seed.

        Returns:
            The seed.
        """
        seed = np.random.choice(a=range(self.low, self.high), replace=False)
        return seed

    def generate_seed_from_seed(self, seed: int) -> int:
        """Generates a new seed from an input seed.

        Args:
            seed: The input seed.

        Returns:
            The new seed.
        """
        # Create a Generator object with default BitGenerator and seed
        rng = np.random.default_rng(seed=seed)
        # Generate a random number
        number = rng.integers(low=self.low, high=self.high, size=1)
        return number[0]

    def pick_random_int(self, low: int, high: int, seed: int) -> int:
        """Picks a random integer from a range of integers.

        Args:
            low: The lowest integer in the range.
            high: The highest integer in the range.
            seed: The input seed for the bit generator.

        Returns:
            The random integer.
        """
        # Create a Generator object with default BitGenerator and seed
        rng = np.random.default_rng(seed=seed)
        # Generate a random number
        self.number = rng.integers(low=low, high=high, size=1)
        return self.number[0]
