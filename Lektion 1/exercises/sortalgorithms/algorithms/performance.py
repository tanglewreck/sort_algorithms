"""
Defines functions used to measure performance
of sort algorithms.
"""

# pylint: disable=invalid-name

__all__ = ["algorithmPerformance", "sortWrapper", "timeIt"]

import functools
import timeit
from . defaults import ITERATIONS
from . defaults import TIMEIT_ITERATIONS
from . defaults import LIST_LENGTH
from . utils import generateRandomList
from . bubblesortplus import bubbleSortPlus
# from . bubblesort import bubbleSort

def algorithmPerformance(iterations: int = ITERATIONS,
                         algorithm = bubbleSortPlus,
                         listLength: int = LIST_LENGTH) -> tuple:
    """Simple performance test of the sorting
    algorithm, using the average number of swaps
    and comparisons over a large number of runs as
    indicators of efficiency."""

    sumOfSwaps = 0
    sumOfComparisons = 0
    for _ in range(iterations):
        # Generate a random list
        randomList = generateRandomList(listLength=listLength)
        # Sort the list
        (randomList,
         numberOfSwaps,
         numberOfComparisons) = algorithm(randomList)
         # numberOfComparisons) = bubbleSortPlus(randomList)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    meanNumberOfSwaps = sumOfSwaps / iterations
    meanNumberOfComparisons = sumOfComparisons / iterations

    return (meanNumberOfSwaps, meanNumberOfComparisons)


def sortWrapper(algorithm = bubbleSortPlus,
                listLength: int = LIST_LENGTH) -> None:
    """Wrapper routine used by the timeIt function"""
    randomList = generateRandomList(listLength=listLength)
    algorithm(randomList)


def timeIt(timeitIterations: int = TIMEIT_ITERATIONS,
           algorithm = bubbleSortPlus,
           listLength: int= LIST_LENGTH) -> None:
    """Time main()"""
    f = functools.partial(sortWrapper,
                          algorithm=algorithm,
                          listLength=listLength)
    t = timeit.Timer(f)
    elapsed = t.timeit(timeitIterations)
    return elapsed
