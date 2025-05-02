"""
    performance.py:

    Defines functions used to measure performance
    of sort algorithms.
"""

import functools
import timeit
import numpy as np
from . utils import generate_random_list
from . defaults import ITERATIONS
from . defaults import TIMEIT_ITERATIONS
from . defaults import TIMEIT_REPEAT

__all__ = ["algo_perf",
           "algorithm_perf",
           "algorithm_performance",
           "do_measurements",
           "time_it",
           "time_it_full"]


def algo_perf(algorithm, list_length):
    """sort list using an algorithm, 
    return (# comparisons, # swaps)"""
    elapsed = []
    comps = []
    swaps = []
    for _ in range(ITERATIONS):
        random_list = generate_random_list(list_length=list_length)

        (_, no_comps, no_swaps) = algorithm(random_list)
        comps.append(no_comps)
        swaps.append(no_swaps)

        elapsed = time_it_full(algorithm=algorithm,
                                    timeit_repeat=TIMEIT_REPEAT,
                                    timeit_iterations=TIMEIT_ITERATIONS,
                                    list_length=list_length)
    return (elapsed, comps, swaps)


def algorithm_perf(algorithm, list_length):
    """sort list using an algorithm, 
    return (# comparisons, # swaps)"""
    elapsed = []
    comps = []
    swaps = []
    for _ in range(ITERATIONS):
        random_list = generate_random_list(list_length=list_length)
        (_, no_comps, no_swaps) = algorithm(random_list)
        comps.append(no_comps)
        swaps.append(no_swaps)

        (elapsed_mean, _) = time_it(algorithm=algorithm,
                                    timeit_repeat=TIMEIT_REPEAT,
                                    timeit_iterations=TIMEIT_ITERATIONS,
                                    list_length=list_length)
        elapsed.append(elapsed_mean)
    return (np.mean(elapsed), np.mean(comps), np.mean(swaps))


def algorithm_performance(algorithm,
                          iterations: int,
                          list_length: int) -> tuple:
    """Performance test of a sorting algorithm in terms 
    number of comparisons and swaps.

    - iterations: number of times to execute the algorithm on randomly
      generated lists of interger (of length list_length)
    - algorithm: a function that takes a list to be sorted as argument
    - list_length: number of integers to generate for each run
    - returns mean and stddev of number of comparisons and swaps
    """

    # Initialise data-structures
    swaps = np.zeros(iterations)
    comparisons = np.zeros(iterations)

    # Run the algorithm repeatedly an collect number of comparisons and number
    # of swaps made during each run
    for k in range(iterations):
        # Generate a random list (using np.random.randint())
        random_list = generate_random_list(list_length=list_length)
        # Sort the list
        (random_list, no_comparisons, no_swaps) = algorithm(random_list)
        swaps[k] = no_swaps
        comparisons[k] = no_comparisons

    # Compute and return means and standard deviations
    # mean_comparisons = np.mean(comparisons)
    # mean_swaps = np.mean(swaps)
    # stddev_comparisons = np.sqrt(np.var(comparisons))
    # stddev_swaps = np.sqrt(np.var(swaps))
    mean_comparisons = comparisons.mean()
    mean_swaps = swaps.mean()
    stddev_comparisons = comparisons.std()
    stddev_swaps = swaps.std()

    if __debug__:
        print(f"list_length: {list_length}")
        print(f"mean_comparisons: {mean_comparisons} ± {stddev_comparisons}")
        print(f"mean_swaps: {mean_swaps} ± {stddev_swaps}")

    return (mean_comparisons, mean_swaps, stddev_comparisons, stddev_swaps)


def sort_wrapper(algorithm, list_length: int) -> None:
    """Wrapper routine used by the time_it function"""
    random_list = generate_random_list(list_length=list_length)
    algorithm(random_list)


def time_it(algorithm,
            timeit_repeat: int,
            timeit_iterations: int,
            list_length: int) -> tuple:
    """measure execution time (elapsed) using timeit.repeat()"""
    f = functools.partial(sort_wrapper,
                          algorithm=algorithm,
                          list_length=list_length)
    t = timeit.Timer(f)
    times = t.repeat(repeat=timeit_repeat, number=timeit_iterations)
    return (np.mean(times), np.sqrt(np.var(times)))


def time_it_full(algorithm,
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


def do_measurements(algorithm,
                    list_length: int,
                    iterations: int,
                    timeit_repeat: int,
                    timeit_iterations: int) -> tuple:
    """do_measurements():

        returns three dictionaries, elapsed, comp, swaps,
        each with the keys 'mean' and 'stddev'.
    """
    if __debug__:
        print(
            f"Measuring performance of {algorithm.__name__} "
            f"({TIMEIT_ITERATIONS} iterations):")

    # Initialise three dicts for collecting
    # means and stddevs
    elapsed = {}
    comp = {}
    swaps = {}

    # Measure execution time
    (elapsed['mean'],
     elapsed['stddev']) = time_it(algorithm=algorithm,
                                  timeit_repeat=timeit_repeat,
                                  timeit_iterations=timeit_iterations,
                                  list_length=list_length)
    # Measure performance in terms of (mean) number of
    # swaps and (mean) number of comparisons
    (comp['mean'],
     swaps['mean'],
     comp['stddev'],
     swaps['stddev']) = algorithm_performance(algorithm=algorithm,
                                              iterations=iterations,
                                              list_length=list_length)
    if __debug__:
        print(f"Elapsed = {elapsed['mean']:6.4f} "
              f"± {elapsed['stddev']:6.4f} seconds"
              f"({TIMEIT_ITERATIONS} iterations)")
        print(f"Comparisons: {comp['mean']:6.4f} "
              f"± {comp['stddev']:6.4f} ({ITERATIONS} iterations)")
        print(f"Swaps: {swaps['mean']:6.4f} "
              f"± {swaps['stddev']:6.4f} ({ITERATIONS} iterations)")
        print("Done.")
        print("")

    return (elapsed, comp, swaps)
