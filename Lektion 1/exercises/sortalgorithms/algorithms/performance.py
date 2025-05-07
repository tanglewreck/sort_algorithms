"""
    NAME
        performance.py
    DESCRIPTION
        Defines functions used to measure performance
        of sort algorithms.
    DATE
        2025-05-04
"""

import timeit
from collections.abc import Callable
from functools import partial
# pylint: disable=unused-import
import numpy as np
from pandas import DataFrame
from . defaults import ALGORITHMS, ALGOSALL
from . defaults import bubblesort, bubblesort_nocopy
from . defaults import bubblesort2, bubblesort2_nocopy
from . defaults import insertionsort, insertionsort2, insertionsort3
from . defaults import ITERATIONS
from . defaults import LENGTH_DEFAULT
from . defaults import LIST_LENGTHS
from . defaults import LOWER, UPPER
from . defaults import TIMEIT_ITERATIONS
from . defaults import TIMEIT_REPEAT
from . utils import generate_random_list
from . utils import debug_msg, err_msg, sys_msg
# pylint: enable=unused-import

__all__ = ["algo_perf",
           "genlists",
           "measure",
           "time_it_repeat",
           "time_it_repeat_2"]


def genlists(low: int = LOWER, high: int = UPPER,
             size = (ITERATIONS, LENGTH_DEFAULT),
             dtype = int):
    """
        NAME
            genlists
        DESCRIPTION
            Basically a wrapper around np.random.randint with
            default values provided.
    """
    return np.random.randint(low, high, size, dtype)


# pylint: disable=too-many-locals
def measure(ldata: np.array, algo: Callable,
            nlists: int = ITERATIONS, llength: int = 10,
            verbose = False, veryverbose = False):
    """
        Measure algorithm performance in terms of execution time ("t"),
        number of comparisons ("comps"), and number of swaps ("swaps").

        Parameters
        ----------
            ldata : numpy.ndarray – A two-dimensional numpy array containing
                    lists of numbers (one list per row); the number of lists
                    (rows) must be >= nlists; the length of each list (number
                    of columns) must >= llength
            algo : Callable/function used to sort the lists
            nlists : int – Number of lists (number of rows in ldata) to process
            llength : int – List-length (number of columns in ldata)
            verbose : bool – if True, diagnostic/debug messages get printed

        Returns
        -------
        DataFrame({'algorithm': np.repeat(algo.__name__, nlists),
                   'length': np.repeat(llength, nlists),
                   't': t, 'comps': comps, 'swaps': swaps})

    """
    # Initialise three lists to contain measurement data
    t, comps, swaps = [], [], []
    try:
        if verbose:
            print(f"algorithm {algo.__name__}")
            print(f"ldata.shape {ldata.shape}")
            print(f"llength {llength}")
            print(f"nlists {nlists}")
            print()
        # Sanity check
        try:
            if llength > ldata.shape[1]:
                errormsg = f"llength > (list length in ldata ({ldata.shape[1]}))"
                raise IndexError(errormsg)
        except AttributeError as exception:
            err_msg(f"ldata should be a numpy.ndarray: {repr(exception)}")
            raise
        except IndexError as exception:
            err_msg(f"{repr(exception)}")
        # Measurements go here (number of measurements = nlists)
        for iteration in range(nlists):
            # Extract a list of suitable length from the data array
            l = ldata[iteration][:llength]
            if veryverbose:
                print(f"List to be sorted: {l}")
            # Measure number of comparisons and swaps
            _, c, s = algo(l)
            # Measure execution time
            f = partial(algo, l)
            timer = timeit.Timer(f)
            # Append results to data lists
            comps.append(c)
            swaps.append(s)
            t.append(timer.timeit(1))
        if veryverbose:
            print()
            print(f"t = {t}")
            print(f"comps = {comps}")
            print(f"swaps = {swaps}")
            print()
        if verbose:
            print(f"t.mean = {np.mean(t) / 1e-3:01.4f} ± {np.std(t) / 1e-3:01.4f} ms")
            print(f"comps.mean = {np.mean(comps):01.2f} ± {np.std(comps):01.2f}")
            print(f"swaps.mean = {np.mean(swaps):01.2f} ± {np.std(swaps):01.2f}")
            print()
    except AttributeError as exception:
        err_msg("AttributeError:")
        err_msg(f"{repr(exception)}")
        raise
    except IndexError as exception:
        err_msg("IndexError:")
        err_msg(f"{repr(exception)}")
        raise
    # Create and return a dataframe with the measurements as columns
    return DataFrame({'algorithm': np.repeat(algo.__name__, nlists),
                      'length': np.repeat(llength, nlists),
                      't': t, 'comps': comps, 'swaps': swaps})


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


#def algo_perf_2(algorithm: Callable,
#                lists: int,
#                iterations: int):
#    """
#        NAME
#            algo_perf
#        DESCRIPTION
#            Repeatedly sort lists of numbers using a specified
#            sort-algorithm function
#            (a Callable (function) object),...
#            return (# comparisons, # swaps)"""
#    comps = []
#    swaps = []
#    for _ in range(iterations):
#        random_list = generate_random_list(list_length)
#        (_, no_comps, no_swaps) = algorithm(random_list)
#        comps.append(no_comps)
#        swaps.append(no_swaps)
#    return np.array(comps), np.array(swaps)
#
#
def sort_wrapper(algorithm: Callable, list_length: int) -> None:
    """Wrapper routine used by the time_it* functions"""
    random_list = generate_random_list(list_length)
    algorithm(random_list)


def time_it_repeat(algorithm: Callable,
                   timeit_repeat: int,
                   timeit_iterations: int,
                   list_length: int) -> tuple:
    """measure execution time (elapsed) using timeit.repeat()"""
    f = partial(sort_wrapper,
                          algorithm=algorithm,
                          list_length=list_length)
    t = timeit.Timer(f)
    times = t.repeat(repeat=timeit_repeat, number=timeit_iterations)
    return np.array(times)


#def sort_wrapper_2(algorithm: Callable,
#                   list_data: np.array) -> None:
#    """Wrapper routine used by the time_it* functions"""
#    random_list = generate_random_list(list_length)
#    # random_list = get_next_list
#    algorithm(random_list)


def time_it_repeat_2(algorithm: Callable,
        lists: np.array,
        timeit_repeat: int = TIMEIT_REPEAT,
        timeit_iterations: int = TIMEIT_ITERATIONS
) -> tuple:
    """measure execution time (elapsed) using timeit.repeat()"""
    #f = partial(sort_wrapper,
    #                      algorithm=algorithm,
    #                      list_length=list_length)
    times = []
    for k in timeit_repeat:
        list_to_sort = lists[k]
        f = f"{algorithm}({list_to_sort})"
        t = timeit.Timer(f)
        times.append(t.timeit(timeit_iterations))
    return np.array(times)


#
#
#def time_it(algorithm: Callable,
#            timeit_repeat: int,
#            timeit_iterations: int,
#            list_length: int) -> tuple:
#    """measure execution time (elapsed) using timeit.repeat()"""
#    f = partial(sort_wrapper,
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
