"""This is the script which launches Workload-Runner.

Please see the README.md file for example command-lines.
"""

import importlib
from typing import Tuple

from utils.args import Args
from utils.logger import Logger
from utils.parallel import Parallel
from utils.paths import Paths
from utils.randomizer import Randomizer
from utils.timer import Timer


def main():
    args_parser = Args()
    logger = Logger()
    parallel = Parallel()
    paths = Paths()
    randomizer = Randomizer()
    timer = Timer()
    parser = args_parser.get_parser()
    args = parser.parse_args()
    bool_args = args_parser.get_bool_args(args)
    bins_path = paths.bins_path
    wl_module = {}
    wl_config = {}
    args.workload = set(args.workload)
    for wl in args.workload:
        wl_module_str = paths.get_wl_module(workload=wl)
        wl_module[wl] = importlib.import_module(wl_module_str).Workload()
        wl_config_str = paths.get_wl_config(workload=wl)
        wl_config[wl] = importlib.import_module(wl_config_str)
    logger.run_pre_exec(
        wl_list=args.workload,
        is_iter=bool_args["is_iter"],
        is_random=bool_args["is_random"],
    )
    if bool_args["is_random"]:
        start_seed = randomizer.generate_seed()
    else:
        start_seed = args.seed
    current_seed = start_seed
    pass_count = 0
    task_count = 0
    start_time = timer.press_timer()

    def loop_execution(
        current_seed: int, iter_id: int, task_count: int, pass_count: int
    ) -> Tuple[int, int, int, int]:
        """Execute steps for running a regression test for the given input iterations/runtime.

        Args:
            current_seed: The current iteration seed.
            iter_id: The current iteration ID.
            task_count: Counter for recording the number of tasks run.
            pass_count: Counter for recording the number of tasks that passed.

        Returns:
            The updated input arguments.

        Raises:
            FileNotFoundError: If output log file is not found.
        """
        log_dict = {}
        attributes_dict = {}
        for wl in args.workload:
            attributes_dict[wl] = wl_config[wl].attributes[
                randomizer.pick_random_int(
                    low=0, high=len(wl_config[wl].attributes), seed=current_seed
                )
            ]
            subdir_path, log_paths = logger.run_exec(
                seed=current_seed, workload=wl, current_iter=iter_id
            )
            log_dict[wl] = log_paths[0]
            parallel.start_process(
                func=wl_module[wl].run(
                    seed=current_seed,
                    bin_path=wl_config[wl].bin_path[attributes_dict[wl]],
                    stdout_path=log_paths[0],
                    stderr_path=log_paths[1],
                )
            )
        parallel.wait()
        for wl, log_path in log_dict.items():
            try:
                is_pass = wl_module[wl].process_output(stdout_path=log_path)
            except FileNotFoundError:
                logger.print_error("Couldn't read output file!")
            pass_count += logger.run_post_exec(
                is_pass=is_pass,
                log_paths=log_paths,
                attribute=attributes_dict[wl],
                iter_id=iter_id,
            )
            task_count += 1
        current_seed = randomizer.generate_seed_from_seed(seed=current_seed)
        return current_seed, iter_id, task_count, pass_count

    if bool_args["is_iter"]:
        for iter_id in range(1, args.iteration + 1):
            logger.print_iter(
                current_iter=iter_id, total_iter=args.iteration, seed=current_seed
            )
            current_seed, iter_id, task_count, pass_count = loop_execution(
                current_seed=current_seed,
                iter_id=iter_id,
                task_count=task_count,
                pass_count=pass_count,
            )
    else:
        iter_id = 0
        iter_time = 0
        while (
            timer.is_time_remaining
            and timer.time_remaining(start_time=start_time, end_time=args.time)
            > iter_time
        ):
            iter_id += 1
            iter_start_time = timer.press_timer()
            logger.print_time(
                time_left=timer.time_remaining(
                    start_time=start_time, end_time=args.time
                ),
                total_time=args.time,
                seed=current_seed,
            )
            current_seed, iter_id, task_count, pass_count = loop_execution(
                current_seed=current_seed,
                iter_id=iter_id,
                task_count=task_count,
                pass_count=pass_count,
            )
            iter_end_time = timer.press_timer()
            iter_time = iter_end_time - iter_start_time
    end_time = timer.press_timer()
    total_time = end_time - start_time
    total_iter = iter_id
    logger.print_summary(
        pass_count=pass_count,
        task_count=task_count,
        total_iter=total_iter,
        total_time=total_time,
    )


if __name__ == "__main__":
    main()
