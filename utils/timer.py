"""This module contains functions related to time-keeping in Workload-Runner. 

Typical usage example:

  timer = Timer()
  start_time = timer.press_timer()
  end_time = timer.press_timer()
  time_taken = end_time - start_time
"""

import time


class Timer:
    """Class definition for handling Workload-Runner's time-keeping.

    Attributes:
        is_time_remaining: Whether there is time left in the regression test.
    """

    def __init__(self):
        """Initializes an instance from the Timer class."""
        self.is_time_remaining = True

    def press_timer(self) -> float:
        """Records the current time.

        Returns:
            The current time in seconds.
        """
        return time.time()

    def time_remaining(self, start_time: float, end_time: float) -> float:
        """Calculates how much time is remaining from a start time and an end time.

        Args:
            start_time: The start time in seconds.
            end_time: The end time in seconds.

        Returns:
            The time remaining in seconds.
        """
        time_elapsed = time.time() - start_time
        if end_time - time_elapsed <= 0:
            self.is_time_remaining = False
        return end_time - time_elapsed
