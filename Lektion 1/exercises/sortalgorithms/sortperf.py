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

__all__ = ["sortperf"]

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

from algorithms.collect import collect_data

from algorithms.performance import do_measurements
from algorithms.performance import algorithm_perf
from algorithms.performance import algo_perf
from algorithms.performance import time_it_full

from algorithms.plot import plot_data


def sortperf() -> None:
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

    # Collect data:
    #       df_t        execution time
    #       df_cs       number of comparisons and swaps
    #       df          computed averages
    (df_t, df_cs, df) = collect_data()

    # Save the dataframes to disk
    df_t.to_csv("sortperf_t.csv", mode="w", index=False)
    df_cs.to_csv("sortperf_cs.csv", mode="w", index=False)
    df.to_csv("sortperf.csv", mode="w", index=False)


    # Plot data
    try:
        # plot_data(df, columns=["t"])
        # plot_data(df, columns=["comps"])
        # plot_data(df, columns=["swaps"])
        # plot_data(df, columns=["t", "comps"])
        plot_data(df, columns=["t", "comps", "swaps"])
    except ValueError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception


if __name__ == "__main__":
    # sortperf_elapsed()
    sortperf()
