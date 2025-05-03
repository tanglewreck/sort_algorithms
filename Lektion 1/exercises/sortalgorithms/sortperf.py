#!/usr/bin/env python3 -O
"""
    NAME
        sortperf.py
    USAGE
        python [-O] sortperf.py
        python -m sortperf sortperf.py
    DESCRIPTION
        Measure and plot performance data
        of sorting algorithms.
    DATE
        2025-02-19
    VERSION
        2025-05-03
"""

# pylint: disable=consider-using-dict-items
# pylint: disable=unused-import

__all__ = ["sortperf_elapsed",
           "sortperf_comps_swaps"]

import time
# pylint: disable=import-error
import ipdb
# pylint: enable=import-error
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from algorithms.defaults import ALGORITHMS
from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTHS
from algorithms.defaults import ITERATIONS
from algorithms.defaults import TIMEIT_ITERATIONS
from algorithms.defaults import TIMEIT_REPEAT

from algorithms.collect import collect_elapsed
from algorithms.collect import collect_comps_swaps

from algorithms.performance import do_measurements
from algorithms.performance import algorithm_perf
from algorithms.performance import algo_perf
from algorithms.performance import time_it_full

from algorithms.plot import plot_elapsed


def sortperf_elapsed() -> None:
    """
        NAME
            sortperf_elapsed()
        DESCRIPTION
            Measure and plot execution time
            of sort algorithms.

            Configuration parameters (list lengths, number of iterations,
            etc.) be imported from algorithms.defaults.
    """

    # Print some info about this run.
    print("Measuring execution time")
    print(f"Number of iterations (timeit): {TIMEIT_ITERATIONS}\n"
          f"Number of repeats (timeit): {TIMEIT_REPEAT}\n"
          f"List lengths: {[int(k) for k in list(LIST_LENGTHS)]}")
    print("Algorithms:")
    for algo in ALGORITHMS:
        print(f"\t{algo.__name__}")
    print()

    # Collect execution time data
    (df_elapsed, df_elapsed_means) = collect_elapsed()
    # Save the dataframes
    df_elapsed.to_csv("sortperf_elapsed.csv", mode="w", index=False)
    df_elapsed_means.to_csv("sortperf_elapsed_means.csv", mode="w", index=False)

    # ipdb.set_trace()
    # breakpoint()

    # Plot elapsed
    plot_elapsed(df_elapsed_means)


def sortperf_comps_swaps() -> None:
    """
        NAME
            sortperf_comps_swaps()
        DESCRIPTION
            Measure and plot number of comparisons,
            and number of swaps of sort algorithms.

            Configuration parameters (list lengths, number of iterations,
            etc.) be imported from algorithms.defaults.
    """
    # Print some info about this run.
    print("Measuring number of comparisons and swaps")
    print(f"Number of iterations: {ITERATIONS} \n"
          f"List lengths: {[int(k) for k in list(LIST_LENGTHS)]}")
    print("Algorithms:")
    for algo in ALGORITHMS:
        print(f"\t{algo.__name__}")
    print()

    # Collect execution time data
    # (df_elapsed, df_elapsed_means) = collect_elapsed()
    # Save the dataframes
    # df_elapsed.to_csv("sortperf_elapsed.csv", mode="w", index=False)
    # df_elapsed_means.to_csv("sortperf_elapsed_means.csv", mode="w", index=False)

    # ipdb.set_trace()
    # breakpoint()

    # Plot elapsed
    # plot_elapsed(df_elapsed_means)


if __name__ == "__main__":
    sortperf_elapsed()
    sortperf_comps_swaps()
