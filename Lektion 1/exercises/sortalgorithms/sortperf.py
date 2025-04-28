#!/usr/bin/env python3 -O

"""
SYNOPSIS
python [-O] sortperf.py

DESCRIPTION
Measure performance of sorting algorithms.

DATE
2025-02-19

NOTE: run with '-O' to get rid of excessive output

"""

# pylint: disable=unused-import
# pylint: disable=consider-using-dict-items

import time
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

from algorithms.performance import do_measurements
from algorithms.performance import algorithm_perf
from algorithms.plot import do_plots


def main() -> None:
    """
    Measure execution time, mean number of comparisons
    and mean number of swaps of sort algorithms.
    """

    print(f"Number of iterations: {ITERATIONS} \n"
          f"Number of iterations (timeit): {TIMEIT_ITERATIONS}\n"
          f"Number of repeats (timeit): {TIMEIT_REPEAT}\n"
          f"List lengths: {[int(k) for k in list(LIST_LENGTHS)]}\n")
    print("Algorithms:")
    for algo in ALGORITHMS:
        print(algo.__name__)
    print()

    # Initialise data-structure:
    #     data -> {function}
    #                 |-> {name/category}
    #                          |-> {list-length}
    #                                    |-> {'mean', 'stddev'}
    data = {}
    categories = ['elapsed', 'comp', 'swaps']
    for algo in ALGORITHMS:
        data[algo] = {'algorithm': algo.__name__}
        for category in categories:
            data[algo][category] = {'name': category}
            for list_length in LIST_LENGTHS:
                data[algo][category][list_length] = {'mean': 0.0,
                                                     'stddev': 0.0}

    # Collect data (means and stddevs for each data category)
    for list_length in LIST_LENGTHS:
        print(f"Measuring list-length {list_length}", end="...")
        for algo in ALGORITHMS:
            (data[algo]['elapsed'][list_length],
             data[algo]['comp'][list_length],
             data[algo]['swaps'][list_length]) = \
                     do_measurements(algo,
                                     list_length,
                                     iterations=ITERATIONS,
                                     timeit_repeat=TIMEIT_REPEAT,
                                     timeit_iterations=TIMEIT_ITERATIONS)
        print("done")
    print()
    time.sleep(1)

    # Collect data into a dictionary consisting of equal length
    # lists for algorithm, list-length, elapsed, comps, and swaps
    perf_data = {}
    for algo in ALGORITHMS:
        for list_length in LIST_LENGTHS:
            (elapsed, comps, swaps) = algorithm_perf(algo, list_length)

            # Append
            perf_data.setdefault('algorithm', []).append(algo.__name__)
            perf_data.setdefault('list_length', []).append(list_length)
            perf_data.setdefault('elapsed', []).append(elapsed)
            perf_data.setdefault('comps', []).append(comps)
            perf_data.setdefault('swaps', []).append(swaps)
    np.set_printoptions(precision=4, suppress=True)
    
    # Create a dataframe from the performance data
    df = DataFrame(perf_data,
                           columns=["algorithm",
                                    "list_length",
                                   "elapsed",
                                   "comps",
                                   "swaps"])
    print("df:")
    print(df)
    # print()
    # print(df["algorithm"])
    # print("bubblesort elapsed")
    # print(df.loc[df.algorithm == "bubblesort", "elapsed"])
    # print()
    for algo in ALGORITHMS:
        print(f"algorithm: {algo.__name__}")
        for list_length in LIST_LENGTHS:
            d = df.loc[df.algorithm == algo.__name__].loc[
                       df.list_length == list_length,
                       "comps"]
            print(f"comps mean ({list_length}): "
                  f"{d.mean()} ± {d.std()}")
        print()
    quit()

    # Print results
    # for algo in ALGORITHMS:
    for algo in data:
        print("=" * 40, sep="")
        print(f"algorithm: {data[algo]['algorithm']}")
        print("=" * 40, sep="")
        for list_length in LIST_LENGTHS:
            print(f"list length: {list_length}")
            for category in categories:
                print(f"\t{category}: "
                      f"{data[algo][category][list_length]['mean']:6.4f} "
                      f"± {data[algo][category][list_length]['stddev']:6.4f}")
            print("-" * 40, sep="")
        print("\n\n")

    # Plot results
    do_plots(data, categories)

    return data


if __name__ == "__main__":
    perfdata = main()
