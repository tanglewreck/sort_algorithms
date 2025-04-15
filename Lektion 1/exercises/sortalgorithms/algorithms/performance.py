"""
Defines functions used to measure performance
of sort algorithms.
"""

# pylint: disable=invalid-name

__all__ = ["algorithmPerformance", "sortWrapper", "timeIt"]

import functools
import timeit
from . defaults import ITERATIONS, TIMEIT_ITERATIONS
from . utils import generateRandomList
from . bubblesortplus import bubbleSortPlus
# from . bubblesort import bubbleSort

def algorithmPerformance(iterations: int = ITERATIONS,
                         algorithm = bubbleSortPlus) -> tuple:
    """Simple performance test of the sorting
    algorithm, using the average number of swaps
    and comparisons over a large number of runs as
    indicators of efficiency."""

    sumOfSwaps = 0
    sumOfComparisons = 0
    for _ in range(iterations):
        # Generate a random list
        intList = generateRandomList()
        # Sort the list
        (intList,
         numberOfSwaps,
         numberOfComparisons) = algorithm(intList)
         # numberOfComparisons) = bubbleSortPlus(intList)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    meanNumberOfSwaps = sumOfSwaps / iterations
    meanNumberOfComparisons = sumOfComparisons / iterations

    return (meanNumberOfSwaps, meanNumberOfComparisons)


def sortWrapper(algorithm = bubbleSortPlus) -> None:
    """Wrapper routine used by the timeIt function"""
    randomList = generateRandomList()
    algorithm(randomList)


def timeIt(timeitIterations: int = TIMEIT_ITERATIONS, algorithm =
           bubbleSortPlus) -> None:
    """Time main()"""
    f = functools.partial(sortWrapper, algorithm=algorithm)
    t = timeit.Timer(f)
    elapsed = t.timeit(timeitIterations)
    return elapsed
