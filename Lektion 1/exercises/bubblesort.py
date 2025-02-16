# coding: utf-8
"""
bubblesort 

Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
import functools
import timeit
import numpy as np

# Number of numbers in the list
N = 100
# Min size of a number in the list
MIN = 1
# Max size of a number in the list
MAX = 100_000
# Number of iterations while measuring performance
ITERATIONS = 20_000
# Number of iterations using the timeite module
TIMEIT_ITERATIONS = 1_000_000


def generateRandomList(minimum:int = MIN,
                       maximum:int = MAX,
                       numbersToGenerate:int = N,
                       verbose=False) -> list:
    """
    Generate random integers btw min (inclusive) and max (inclusive).
    """
    try:
        randomList = [int(n) for n in np.random.randint(minimum, maximum, numbersToGenerate)]
        if verbose:
            print(randomList)
        return randomList

    except ValueError as e:
        print(e)
        raise SystemExit(1) from e


def bubbleSort(theList: list, verbose = False):
    """Bubblesort"""
    theListCopy = theList + []
    swapped = True
    numberOfSwaps = 0
    numberOfComparisons = 0
    iteration = 1
    while swapped:
        swapped = False
        if verbose:
            print(f"iteration: {iteration}")
        for index in range(len(theListCopy) - 1):
            i = theListCopy[index]
            i1 = theListCopy[index + 1]
            numberOfComparisons += 1
            if verbose:
                print(f"index: {index}:")
                print(f"{theListCopy} ", end="")
            if theListCopy[index] > theListCopy[index + 1]:
                swapped = True
                numberOfSwaps += 1
                if verbose:
                    print(f"---> ({i} > {i1}) swapped  <--- {theListCopy}")
                (theListCopy[index],
                 theListCopy[index + 1]) = (theListCopy[index + 1],
                                            theListCopy[index])
            else:
                if verbose:
                    print(f"---> ({i} <= {i1}) no swap <--- {theListCopy}")
        if verbose:
            print()
        iteration += 1
    #print(f"Number of swaps: {numberOfSwaps}")
    return (theListCopy, numberOfSwaps, numberOfComparisons)


def algorithmPerformance(iterations: int = ITERATIONS) -> tuple:
    """Simple performance test of the sorting
    algorithm, using the average number of swaps
    and comparisons over a large number of runs as
    indicators of efficiency."""

    sumOfSwaps = 0
    sumOfComparisons = 0
    for _ in range(iterations):
        # Generate a random list
        randomList = generateRandomList(MIN, MAX, N)
        # Sort the list
        (randomList,
         numberOfSwaps,
         numberOfComparisons) = bubbleSort(randomList, verbose=False)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    return (sumOfSwaps / iterations,
            sumOfComparisons / iterations)


def bubbleSortWrapper():
    randomList = generateRandomList(MIN, MAX, N, verbose=False)
    bubbleSort(randomList)


def timeIt(timeitIterations: int = TIMEIT_ITERATIONS) -> None:
    """Time main()"""
    f = functools.partial(bubbleSortWrapper)
    t = timeit.Timer(f)
    elapsed = t.timeit(timeitIterations)
    print(f"elapsed = {elapsed} ({timeitIterations} iterations)")


def main(minimum = MIN, maximum = MAX, numbersToGenerate = N):
    """main"""
    # Measure execution time
    timeIt()
    # Measure performance in terms of (mean) number of
    # swaps and (mean) number of comparisons
    (meanNumberOfSwaps,
     meanNumberOfComparisons) = algorithmPerformance(
         iterations=ITERATIONS)
    # Print results
    print(f"list-length: {N}, iterations: {ITERATIONS}")
    print(f"Mean number of swaps: {meanNumberOfSwaps}")
    print(f"Mean number of comparisons: {meanNumberOfComparisons}")

    # Sort and display once to make verify that the algorithm works
    randomNumbers = generateRandomList(MIN, MAX, N, verbose=False)
    # Sort the list and collect statistics
    (sortedRandomNumbers, _, _) = bubbleSort(randomNumbers, verbose=False)
    print(f"in = {randomNumbers}")
    print(f"out = {sortedRandomNumbers}")

if __name__ == "__main__":
    main()

