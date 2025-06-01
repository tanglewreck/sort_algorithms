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

# xxxpylint: disable=consider-using-dict-items
# xxxpylint: disable=unused-import

# __all__ = ["sortperf"]

# pylint: disable=import-error
import ipdb
# pylint: enable=import-error

#from algorithms.collect import collect_data
#from algorithms.defaults import ALGORITHMS
#from algorithms.defaults import LIST_LENGTHS
#from algorithms.defaults import ITERATIONS
#from algorithms.defaults import TIMEIT_ITERATIONS
#from algorithms.defaults import TIMEIT_REPEAT
#from algorithms.plot import plot_data
from algorithms.insertionsort import insertionsort_new
from algorithms.utils import generate_random_list


#def sortperf() -> None:
#    """
#        NAME
#            sortperf_elapsed()
#        DESCRIPTION
#            Measure and plot execution time
#            of sort algorithms.
#
#            Configuration parameters (list lengths, number of iterations,
#            etc.) be imported from algorithms.defaults.
#    """
#
#    # Print some info about this run.
#    print("Measuring performance...")
#    print(f"Number of iterations: {ITERATIONS}\n"
#          f"Number of iterations (timeit): {TIMEIT_ITERATIONS}\n"
#          f"Number of repeats (timeit): {TIMEIT_REPEAT}\n"
#          f"List lengths: {[int(k) for k in list(LIST_LENGTHS)]}")
#    print("Algorithms:")
#    for algo in ALGORITHMS:
#        print(f"\t{algo.__name__}")
#    print()
#
#    # Collect data:
#    #       df_t        execution time
#    #       df_cs       number of comparisons and swaps
#    #       df          computed averages
#    (df_t, df_cs, df) = collect_data()
#
#    # Save the dataframes to disk
#    df_t.to_csv("sortperf_t.csv", mode="w", index=False)
#    df_cs.to_csv("sortperf_cs.csv", mode="w", index=False)
#    df.to_csv("sortperf.csv", mode="w", index=False)
#
#
#    # Plot data
#    try:
#        # plot_data(df, columns=["t"])
#        # plot_data(df, columns=["comps"])
#        # plot_data(df, columns=["swaps"])
#        # plot_data(df, columns=["t", "comps"])
#        plot_data(df, columns=["t", "comps", "swaps"])
#    except ValueError as exception:
#        print(repr(exception))
#        raise SystemExit(1) from exception
#
#
if __name__ == "__main__":
    l_unsorted = generate_random_list(10)
    print(f"in: {l_unsorted}")
    # ipdb.sset_trace()
    l_sorted, ncomps, nswaps = insertionsort_new(l_unsorted)
    print(f"out: {l_sorted}")
    print(f"ncomps: {ncomps}")
    print(f"nswaps: {nswaps}")
