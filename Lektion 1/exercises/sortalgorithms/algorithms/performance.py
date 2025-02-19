"""
Defines functions used to measure performance
of sort algorithms.
"""

__all__ = ["algorithmPerformance", "sortWrapper", "timeIt"]

import functools
import timeit
from . defaults import ITERATIONS, TIMEIT_ITERATIONS
from . utils import generateRandomList
from . mysortalgorithm import mySortAlgorithm
from . bubblesort import bubbleSort

def algorithmPerformance(iterations: int = ITERATIONS, func = mySortAlgorithm) -> tuple:
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
         numberOfComparisons) = func(intList)
         # numberOfComparisons) = mySortAlgorithm(intList)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    meanNumberOfSwaps = sumOfSwaps / iterations
    meanNumberOfComparisons = sumOfComparisons / iterations

    return (meanNumberOfSwaps, meanNumberOfComparisons)


def sortWrapper(func = mySortAlgorithm) -> None:
    """Wrapper routine used by the timeIt function"""
    randomList = generateRandomList()
    func(randomList)


def timeIt(timeitIterations: int = TIMEIT_ITERATIONS, func = mySortAlgorithm) -> None:
    """Time main()"""
    f = functools.partial(sortWrapper, func=func)
    t = timeit.Timer(f)
    elapsed = t.timeit(timeitIterations)
    return elapsed
