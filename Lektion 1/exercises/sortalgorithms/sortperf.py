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

__all__ = ["sortperf"]

import time

import ipdb
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
from algorithms.performance import algo_perf
from algorithms.performance import time_it_full
from algorithms.plot import do_plots

from algorithms.bubblesort import bubblesort
from algorithms.bubblesortplus import bubblesort_plus

def sortperf() -> None:
    """
    Measure execution time, mean number of comparisons
    and mean number of swaps of sort algorithms.
    """
    def collect_elapsed():
        # Create a list used to contain pd.DataFrame's
        dfs = []
        for algo in ALGORITHMS:
            for length in LIST_LENGTHS:
                # Initialise data dict
                elapsed_data = {'algorithm': np.repeat(algo.__name__,
                                                       TIMEIT_REPEAT),
                                'length': np.repeat(length,
                                                    TIMEIT_REPEAT)}
                # Measure execution time, using time_it_full() which
                # returns a list of floats of length TIMEIT_REPEAT.
                # Add the returned list to the data dict (column-name:
                # "elapsed").
                elapsed = np.array(time_it_full(algorithm=algo,
                                       timeit_repeat=TIMEIT_REPEAT,
                                       timeit_iterations=TIMEIT_ITERATIONS,
                                       list_length=length))
                elapsed_data['elapsed'] = elapsed
                # Convert the data-dict to a DataFrame and append
                # to the list of dataframes.
                df = DataFrame(elapsed_data,
                               columns=["algorithm",
                                        "length",
                                        "elapsed"])
                dfs.append(df)

        # Concatenate the list of dataframes into one
        df = pd.concat(dfs, ignore_index=True)
        return df



    # Print some info about this run.
    print(f"Number of iterations: {ITERATIONS} \n"
          f"Number of iterations (timeit): {TIMEIT_ITERATIONS}\n"
          f"Number of repeats (timeit): {TIMEIT_REPEAT}\n"
          f"List lengths: {[int(k) for k in list(LIST_LENGTHS)]}\n")
    print("Algorithms:")
    for algo in ALGORITHMS:
        print(f"\t{algo.__name__}")
    print()

    # Collect execution time data
    # Create a list used to contain pd.DataFrame's
    dfs = []
    for algo in ALGORITHMS:
        for length in LIST_LENGTHS:
            # Initialise data dict
            elapsed_data = {'algorithm': np.repeat(algo.__name__,
                                                   TIMEIT_REPEAT),
                            'length': np.repeat(length,
                                                TIMEIT_REPEAT)}
            # Measure execution time, using time_it_full() which
            # returns a list of floats of length TIMEIT_REPEAT.
            # Add the returned list to the data dict (column-name:
            # "elapsed").
            elapsed = np.array(time_it_full(algorithm=algo,
                                   timeit_repeat=TIMEIT_REPEAT,
                                   timeit_iterations=TIMEIT_ITERATIONS,
                                   list_length=length))
            elapsed_data['elapsed'] = elapsed
            # Convert the data-dict to a DataFrame and append
            # to the list of dataframes.
            df = DataFrame(elapsed_data,
                           columns=["algorithm",
                                    "length",
                                    "elapsed"])
            dfs.append(df)

    # Concatenate the list of dataframes into one
    df = pd.concat(dfs, ignore_index=True)

    # Save the dataframe to a csv file (overwriting existing file).
    df.to_csv("sortperf.csv", mode="w", index=False)

    # Create a dataframe for averages
    dfs = []
    for algo in ALGORITHMS:
        elapsed_means = np.zeros(len(LIST_LENGTHS))
        for k, length in enumerate(LIST_LENGTHS):
            elapsed_means[k] = df.loc[(df.algorithm==algo.__name__) &
                                      (df.length==length)].elapsed.mean()
        elapsed_data = {'algorithm': algo.__name__,
                        'means': list(zip(LIST_LENGTHS, elapsed_means))}

        elapsed_data_2 = DataFrame({'algorithm': algo.__name__,
                          'length': LIST_LENGTHS,
                          'means': [ df.loc[(df.algorithm==algo.__name__) &
                                            (df.length==length)].elapsed.mean()
                                     for length in LIST_LENGTHS]})
        dfs.append(elapsed_data_2)
    df_means = pd.concat(dfs, ignore_index=True)

    # Save the dataframe to a csv file (overwriting existing file).
    df_means.to_csv("sortperf_elapsed.csv", mode="w", index=False)

    ipdb.set_trace()
    # breakpoint()


    # Plot means
    plt.plot(LIST_LENGTHS, [df_means.loc[df_means.length==L].means for L in LIST_LENGTHS])
    plt.legend([algo.__name__ for algo in ALGORITHMS])
    plt.ylabel("elapsed (ms)")
    plt.xlabel("list length")
    plt.show()

#
#     # Initialise data-structure:
#     #     data -> {function}
#     #                 |-> {name/category}
#     #                          |-> {list-length}
#     #                                    |-> {'mean', 'stddev'}
#     data = {}
#     categories = ['elapsed', 'comp', 'swaps']
#     for algo in ALGORITHMS:
#         data[algo] = {'algorithm': algo.__name__}
#         for category in categories:
#             data[algo][category] = {'name': category}
#             for list_length in LIST_LENGTHS:
#                 data[algo][category][list_length] = {'mean': 0.0,
#                                                      'stddev': 0.0}
#
#     # Collect data (means and stddevs for each data category)
#     for list_length in LIST_LENGTHS:
#         print(f"Measuring list-length {list_length}", end="...")
#         for algo in ALGORITHMS:
#             (data[algo]['elapsed'][list_length],
#              data[algo]['comp'][list_length],
#              data[algo]['swaps'][list_length]) = \
#                      do_measurements(algo,
#                                      list_length,
#                                      iterations=ITERATIONS,
#                                      timeit_repeat=TIMEIT_REPEAT,
#                                      timeit_iterations=TIMEIT_ITERATIONS)
#         print("done")
#     print()
#     time.sleep(1)
#
#     # Collect data into a dictionary consisting of equal length
#     # lists for algorithm, list-length, elapsed, comps, and swaps
#     perf_data = {}
#     elapsed_data = []
#     comps_data = []
#     swaps_data = []
#     algo_data = []
#     list_length_data = []
#     for algo in ALGORITHMS:
#         for list_length in LIST_LENGTHS:
#             (elapsed, comps, swaps) = algo_perf(algo, list_length)
#             elapsed_data.append(elapsed)
#             comps_data.append(comps)
#             swaps_data.append(swaps)
#             algo_data.append(algo.__name__)
#             list_length_data.append(list_length)
#
#             # Append
#             perf_data.setdefault('algorithm', []).append(algo.__name__)
#             perf_data.setdefault('list_length', []).append(list_length)
#             perf_data.setdefault('elapsed', []).append(elapsed)
#             perf_data.setdefault('comps', []).append(comps)
#             perf_data.setdefault('swaps', []).append(swaps)
#
#     # print(len(perf_data['elapsed']))
#     # print(len(perf_data['comps']))
#     # print(len(perf_data['swaps']))
#     # quit()
#     # Create a dataframe from the performance data
#     df = DataFrame(perf_data,
#                            columns=["algorithm",
#                                     "list_length",
#                                    "elapsed",
#                                    "comps",
#                                    "swaps"])
#     # np.set_printoptions(precision=4, suppress=True)
#
#     # print()
#     # print(df["algorithm"])
#     # print("bubblesort elapsed")
#     # print(df.loc[df.algorithm == "bubblesort", "elapsed"])
#     # print()
#     for algo in ALGORITHMS:
#         print(f"algorithm: {algo.__name__}")
#         for list_length in LIST_LENGTHS:
#             d = df.loc[df.algorithm == algo.__name__].loc[
#                        df.list_length == list_length,
#                        "comps"]
#             print(f"comps mean ({list_length}): "
#                   f"{type(d)}")
#             #      f"{d.mean()} ± {d.std()}")
#         print()
#     quit()
#
#     # Print results
#     # for algo in ALGORITHMS:
#     for algo in data:
#         print("=" * 40, sep="")
#         print(f"algorithm: {data[algo]['algorithm']}")
#         print("=" * 40, sep="")
#         for list_length in LIST_LENGTHS:
#             print(f"list length: {list_length}")
#             for category in categories:
#                 print(f"\t{category}: "
#                       f"{data[algo][category][list_length]['mean']:6.4f} "
#                       f"± {data[algo][category][list_length]['stddev']:6.4f}")
#             print("-" * 40, sep="")
#         print("\n\n")
#
#     # Plot results
#     do_plots(data, categories)
#
#     return data
#
#
if __name__ == "__main__":
    sortperf()
