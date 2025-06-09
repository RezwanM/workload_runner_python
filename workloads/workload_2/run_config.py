"""This module contains the run configurations for Workload_2.

Typical usage example:

  wl_2_bin = bin_path["wl_2"]
"""

from pathlib import Path


attributes = ["wl_2"]
bin_path = {
    "wl_2": str(
        Path(__file__)
        .parent.parent.parent.joinpath("bins")
        .joinpath("workload_2")
        .joinpath("wl_2.sh")
        .resolve()
    )
}
