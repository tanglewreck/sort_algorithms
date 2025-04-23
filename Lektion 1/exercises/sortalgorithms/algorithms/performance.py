"""
Defines functions used to measure performance
of sort algorithms.
"""

__all__ = ["algorithm_performance", "sort_wrapper", "time_it"]

import functools
import timeit
from . defaults import ITERATIONS
from . defaults import TIMEIT_ITERATIONS
from . defaults import LIST_LENGTH
from . utils import generate_random_list
from . bubblesortplus import bubblesort_plus
# from . bubblesort import bubbleSort

def algorithm_performance(iterations: int = ITERATIONS,
                         algorithm = bubblesort_plus,
                         list_length: int = LIST_LENGTH) -> tuple:
    """Simple performance test of the sorting
    algorithm, using the average number of swaps
    and comparisons over a large number of runs as
    indicators of efficiency."""

    sum_swaps = 0
    sum_comparisons = 0
    for _ in range(iterations):
        # Generate a random list (using np.random.randint())
        random_list = generate_random_list(list_length=list_length)
        # Sort the list
        (random_list,
         no_swaps,
         no_comparisons) = algorithm(random_list)
         # no_comparisons) = bubblesort_plus(random_list)

        # Update sums
        sum_swaps += no_swaps
        sum_comparisons += no_comparisons

    mean_swaps = sum_swaps / iterations
    mean_comparisons = sum_comparisons / iterations

    return (mean_swaps, mean_comparisons)


def sort_wrapper(algorithm = bubblesort_plus,
                list_length: int = LIST_LENGTH) -> None:
    """Wrapper routine used by the time_it function"""
    random_list = generate_random_list(list_length=list_length)
    algorithm(random_list)


def time_it(timeit_iterations: int = TIMEIT_ITERATIONS,
           algorithm = bubblesort_plus,
           list_length: int= LIST_LENGTH) -> None:
    """measure execution time (elapsed) using the
    timeit module"""
    f = functools.partial(sort_wrapper,
                          algorithm=algorithm,
                          list_length=list_length)
    t = timeit.Timer(f)
    elapsed = t.timeit(timeit_iterations)
    return elapsed
