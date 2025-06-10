# Workload-Runner

The goal of this project was to create a validation tool that can automatically create and execute random, reproducible, and concurrent tests once launched. The tool - *Workload-Runner* - is meant to be accompanied by multiple OS applications (i.e., workloads) which can be used to stress the different IPs of the system. The project was intended to provide a glimpse of the true power of an automated validation framework, and for that reason it employs very simple workloads for demonstration purposes.  

## Preview

    $ python3 ./main.py -wl Workload_1 -wl Workload_2 -iter 2 -seed 123
    ########################################################################################################################
    --------------------------------------------  W o r k l o a d - R u n n e r  -------------------------------------------
    ########################################################################################################################
    ---------------------------------------------------  by Rezwan Matin  --------------------------------------------------
    ---------------------------------------------------  Copyright 2025  ---------------------------------------------------
    ########################################################################################################################
                                                          TEST STARTED
                                                         Now running...
                                                         > Workload_1 <
                                                         > Workload_2 <
                                              Test started with a user-defined seed
                                             Test will run based on input iterations
    ########################################################################################################################
                                                            Seed: 123
                                                        Iteration 1 of 2
                                                         1 wl_1: PASSED!
                                                         1 wl_2: PASSED!
    ########################################################################################################################
                                                            Seed: 113
                                                        Iteration 2 of 2
                                                         2 wl_1: PASSED!
                                                         2 wl_2: PASSED!
    ########################################################################################################################
                                                           TEST ENDED
                                                   Total runtime: 1.16 seconds
                                                       Total iterations: 2
                                                         Total tasks: 4
                                                            Passed: 4
                                                            Failed: 0
    ########################################################################################################################

## Requirements

- Python 3.12.9
- Numpy 2.2.3

## Options

| Flag               | Description                                                 |
| ------------------ | ----------------------------------------------------------- |
| -h, --help         | Display the help information on how to use Workload-Runner. |
| -wl, --workload    | The workload(s) selected for the regression test.           |
| -iter, --iteration | The number of loops the test should run.                    |
| -time, --seed      | The regression runtime (in seconds).                        |
| -seed, --seed      | The input seed.                                             |

**Note:** Workload-Runner requires either iterations or runtime for setting the regression test duration. If both are undefined at input, Workload-Runner will default to running a single iteration of the test.

## Usage

    python3 ./main.py -wl <workload_#1> -wl <workload_#2> ... -iter <iterations> -time <runtime> -seed <seed>

## Examples

### Running *Workload_1* with a random seed for a single iteration (default)

    python3 ./main.py -wl Workload_1

### Running *Workload_1* with a random seed for 3 iterations

    python3 ./main.py -wl Workload_1 -iter 3

### Running *Workload_2* with input runtime and random seed

    python3 ./main.py -wl Workload_2 -time 30

### Running *Workload_1* and *Workload_2* with input iterations and input seed

    python3 ./main.py -wl Workload_1 -wl Workload_2 -iter 5 -seed 123
