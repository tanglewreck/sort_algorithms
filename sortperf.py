#!/usr/bin/env python3
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

# xxxpylint: disable=consider-using-dict-items
# pylint: disable=unused-import
# pylint: disable=unused-variable
# pylint: disable=unused-argument

__all__ = ["sortperf"]

# pylint: disable=import-error
# import ipdb
# pylint: enable=import-error

from algorithms import ALGORITHMS
from algorithms import ITERATIONS
from algorithms import LIST_LENGTHS
from algorithms import LOWER
from algorithms import UPPER
from algorithms import collect_data
from algorithms import plot_data
from algorithms import get_args
# from algorithms import err_msg
# from algorithms import timestamp
# from algorithms import *


def sortperf(low: int = LOWER, high: int = UPPER,
             iterations: int = ITERATIONS,
             listlengths=LIST_LENGTHS,
             algorithms=ALGORITHMS) -> None:
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
    print("Measuring performance...")
    print(f"Number of lists to sort (iterations): {ITERATIONS}\n"
          f"List lengths: {[int(k) for k in list(LIST_LENGTHS)]}")
    print("Algorithms:")
    for algo in algorithms:
        print(f"\t{algo.__name__}")
    print()

    # Collect data (and get two pandas.DataFrames back, one for raw
    # data, and one for averages)
    # (df_raw, df_means) = collect_data()
    (_, df_means) = collect_data()  # Throw away the raw data

    # Save the dataframes to disk
#     now = timestamp()
#     try:
#         df_raw.to_csv(f"lists/sortperf_raw_{now}.csv",
#                       mode="w", index=False)
#         df_means.to_csv(f"lists/sortperf_means_{now}.csv",
#                         mode="w", index=False)
#     except OSError as exception:
#         err_msg("Unable to save dataframes to disk")
#         err_msg(f"{repr(exception)}")
#

    # Plot data
    try:
        # plot_data(df_means, columns=["t"])
        # plot_data(df_means, columns=["comps"])
        # plot_data(df_means, columns=["swaps"])
        # plot_data(df_means, columns=["t", "comps"])
        plot_data(df_means, columns=("t", "comps", "swaps"))
    except ValueError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception


if __name__ == "__main__":
    args = get_args()
    sortperf()
