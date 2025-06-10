"""This module contains functions for parsing and using input arguments for Workload-Runner. 

Typical usage example:

  args_parser = Args()
  args = args_parser.parse_arguments()
  bool_args = args_parser.get_bool_args(args)
"""

import argparse
from typing import Dict


class Args:
    """Class definition for handling Workload-Runner's input arguments."""

    def __init__(self):
        """Initializes an instance from the Args class."""
        pass

    def parse_arguments(self):
        """Parses a set of input arguments.

        Returns:
            The parsed argument object.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-wl",
            "--workload",
            type=str,
            action="extend",
            nargs="+",
            choices=["Workload_1", "Workload_2"],
            help="The workload(s) selected for the regression test",
            required=True,
        )
        group = parser.add_mutually_exclusive_group()
        group.add_argument(
            "-iter",
            "--iteration",
            type=int,
            default=1,
            help="The number of loops the test should run",
        )
        group.add_argument(
            "-time", "--time", type=float, help="The regression runtime (in seconds)"
        )
        parser.add_argument("-seed", "--seed", type=int, help="The input seed")
        args = parser.parse_args()
        return args

    def get_bool_args(self, args: argparse.Namespace) -> Dict[str:bool, str:bool]:
        """Processes a set of boolean variables based on input arguments.

        Args:
            args: A parsed argument object.

        Returns:
            A dictionary of boolean variables.
        """
        is_iter = True
        if args.time:
            is_iter = False
        if args.seed:
            is_random = False
        else:
            is_random = True
        bool_dict = {"is_iter": is_iter, "is_random": is_random}
        return bool_dict
