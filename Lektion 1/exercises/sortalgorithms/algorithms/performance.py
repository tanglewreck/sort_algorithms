"""
    NAME
        performance.py
    DESCRIPTION
        Defines functions used to measure performance
        of sort algorithms.
    DATE
        2025-05-04
"""

import functools
import timeit
from collections.abc import Callable
import numpy as np
from . utils import generate_random_list
# from . defaults import ITERATIONS
# from . defaults import TIMEIT_ITERATIONS
# from . defaults import TIMEIT_REPEAT

__all__ = ["algo_perf",
           "time_it_repeat"]


def algo_perf(algorithm: Callable,
              list_length: int,
              iterations: int):
    """
        NAME
            algo_perf
        DESCRIPTION
            Repeatedly sort lists of numbers using a specified
            sort-algorithm function
            (a Callable (function) object), 
    return (# comparisons, # swaps)"""
    comps = []
    swaps = []
    for _ in range(iterations):
        random_list = generate_random_list(list_length)
        (_, no_comps, no_swaps) = algorithm(random_list)
        comps.append(no_comps)
        swaps.append(no_swaps)
    return np.array(comps), np.array(swaps)


def sort_wrapper(algorithm: Callable, list_length: int) -> None:
    """Wrapper routine used by the time_it* functions"""
    random_list = generate_random_list(list_length)
    algorithm(random_list)


def time_it_repeat(algorithm: Callable,
                   timeit_repeat: int,
                   timeit_iterations: int,
                   list_length: int) -> tuple:
    """measure execution time (elapsed) using timeit.repeat()"""
    f = functools.partial(sort_wrapper,
                          algorithm=algorithm,
                          list_length=list_length)
    t = timeit.Timer(f)
    times = t.repeat(repeat=timeit_repeat, number=timeit_iterations)
    return times
#
#
#def time_it(algorithm: Callable,
#            timeit_repeat: int,
#            timeit_iterations: int,
#            list_length: int) -> tuple:
#    """measure execution time (elapsed) using timeit.repeat()"""
#    f = functools.partial(sort_wrapper,
#                          algorithm=algorithm,
#                          list_length=list_length)
#    t = timeit.Timer(f)
#    times = t.repeat(repeat=timeit_repeat, number=timeit_iterations)
#    return (np.mean(times), np.sqrt(np.var(times)))
#
#
# # # # # # # # # # # # # #
# Not used (to be deleted)
# # # # # # # # # # # # # #
#def do_measurements(algorithm,
#                    list_length: int,
#                    iterations: int,
#                    timeit_repeat: int,
#                    timeit_iterations: int) -> tuple:
#    """do_measurements():
#
#        returns three dictionaries, elapsed, comp, swaps,
#        each with the keys 'mean' and 'stddev'.
#    """
#    if __debug__:
#        print(
#            f"Measuring performance of {algorithm.__name__} "
#            f"({TIMEIT_ITERATIONS} iterations):")
#
#    # Initialise three dicts for collecting
#    # means and stddevs
#    elapsed = {}
#    comp = {}
#    swaps = {}
#
#    # Measure execution time
#    (elapsed['mean'],
#     elapsed['stddev']) = time_it(algorithm=algorithm,
#                                  timeit_repeat=timeit_repeat,
#                                  timeit_iterations=timeit_iterations,
#                                  list_length=list_length)
#    # Measure performance in terms of (mean) number of
#    # swaps and (mean) number of comparisons
#    (comp['mean'],
#     swaps['mean'],
#     comp['stddev'],
#     swaps['stddev']) = algorithm_performance(algorithm=algorithm,
#                                              iterations=iterations,
#                                              list_length=list_length)
#    if __debug__:
#        print(f"Elapsed = {elapsed['mean']:6.4f} "
#              f"± {elapsed['stddev']:6.4f} seconds"
#              f"({TIMEIT_ITERATIONS} iterations)")
#        print(f"Comparisons: {comp['mean']:6.4f} "
#              f"± {comp['stddev']:6.4f} ({ITERATIONS} iterations)")
#        print(f"Swaps: {swaps['mean']:6.4f} "
#              f"± {swaps['stddev']:6.4f} ({ITERATIONS} iterations)")
#        print("Done.")
#        print("")
#
#    return (elapsed, comp, swaps)
