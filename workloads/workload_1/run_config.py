"""This module contains the run configurations for Workload_1.

Typical usage example:

  wl_1_bin = bin_path["wl_1"]
"""

from pathlib import Path


attributes = ["wl_1"]
bin_path = {
    "wl_1": str(
        Path(__file__)
        .parent.parent.parent.joinpath("bins")
        .joinpath("workload_1")
        .joinpath("wl_1.sh")
        .resolve()
    )
}
