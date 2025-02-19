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

def algorithmPerformance(iterations: int = ITERATIONS) -> tuple:
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
         numberOfComparisons) = mySortAlgorithm(intList)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    meanNumberOfSwaps = sumOfSwaps / iterations
    meanNumberOfComparisons = sumOfComparisons / iterations

    return (meanNumberOfSwaps, meanNumberOfComparisons)


def sortWrapper() -> None:
    """Wrapper routine used by the timeIt function"""
    randomList = generateRandomList()
    mySortAlgorithm(randomList)


def timeIt(timeitIterations: int = TIMEIT_ITERATIONS) -> None:
    """Time main()"""
    f = functools.partial(sortWrapper)
    t = timeit.Timer(f)
    elapsed = t.timeit(timeitIterations)
    print(f"elapsed = {elapsed} ({timeitIterations} iterations)")
