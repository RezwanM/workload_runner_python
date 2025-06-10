"""This module contains functions for launching parallel tasks in Workload-Runner. 

Typical usage example:

  parallel = Parallel()
  parallel.start_process(
      func=workloads.workload_1.workload_1.Workload().run(
          seed=123,
          bin_path=".../bins/workload_1/wl_1.sh",
          stdout_path=".../var/log/workload_runner/302cca50069bbc56/workload_1_1_04102025_141638.out",
          stderr_path=".../var/log/workload_runner/302cca50069bbc56/workload_1_1_04102025_141638.err",
      )
  )
  parallel.wait()
"""

from multiprocessing import Process


class Parallel:
    """Class definition for handling Workload-Runner's parallel tasks.

    Attributes:
        process_list: A list of process objects running in parallel.
    """

    def __init__(self):
        """Initializes an instance from the Parallel class."""
        self.process_list = []
        pass

    def start_process(self, func):
        """Adds a process to run in parallel.

        Args:
            func: A function/method/process to be run in parallel.

        """
        p = Process(target=func)
        p.start()
        self.process_list.append(p)

    def wait(self):
        """Waits for all the parallel processes to finish running."""
        for p in self.process_list:
            p.join()
