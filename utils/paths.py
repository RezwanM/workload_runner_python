"""This module contains functions for handling file paths for Workload-Runner. 

Typical usage example:

  paths = Paths()
  bins_path = paths.bins_path
  wl_module_str = paths.get_wl_module(workload="Workload_1")
"""

from pathlib import Path


class Paths:
    """Class definition for handling Workload-Runner's file paths.

    Attributes:
        project_root: The absolute path to Workload_Runner's root directory.
        wl_path: The absolute path to the workloads directory.
        bins_path: The absolute path to the bins directory.
        dir_path: The absolute path to Workload-Runner's log directory.
    """

    def __init__(self):
        """Initializes an instance from the Paths class.

        The instance stores the absolute paths to project files.
        """
        self.project_root = str(Path(__file__).parent.parent.resolve())
        self.wl_path = str(Path(__file__).parent.parent.joinpath("workloads").resolve())
        self.bins_path = str(Path(__file__).parent.parent.joinpath("bins").resolve())
        self.dir_path = str(
            Path(__file__)
            .parent.parent.parent.joinpath("var")
            .joinpath("log")
            .joinpath("workload_runner")
            .resolve()
        )

    def get_wl_module(self, workload: str) -> str:
        """Creates the string for referencing a workload module.

        Args:
            workload: The workload for which to create the module reference string.

        Returns:
            The module reference string.
        """
        module_tup = ("workloads", workload, workload)
        return ".".join(module_tup).lower()

    def get_wl_config(self, workload: str) -> str:
        """Creates the string for referencing a workload's run configuration module.

        Args:
            workload: The workload for which to create the module reference string.

        Returns:
            The module reference string.
        """
        module_tup = ("workloads", workload, "run_config")
        return ".".join(module_tup).lower()
