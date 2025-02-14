# coding: utf-8
"""
bubblesort 

Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
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
        intList = generateRandomList(MIN, MAX, N)
        # Sort the list
        (intList,
         numberOfSwaps,
         numberOfComparisons) = bubbleSort(intList, verbose=False)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    meanNumberOfSwaps = sumOfSwaps / iterations
    meanNumberOfComparisons = sumOfComparisons / iterations

    return (meanNumberOfSwaps, meanNumberOfComparisons)


def main(minium = MIN, maximum = MAX, numbersToGenerate = N):
    """main"""
    myList = generateRandomList(minimum,
                                maximum,
                                numbersToGenerate,
                                verbose=False)
    # Sort the list and collect statistics
    (myList,
     numberOfSwaps,
     numberOfComparisons) = bubbleSort(myList, verbose=False)


if __name__ == "__main__":

    iterations = 1_000_000_000
    t = timeit.Timer("main")
    try:
        elapsed = t.timeit(iterations)
        print(f"elapsed = {elapsed} ({iterations} iterations)")
    except:
        print("EEEEEERRROR")

    # Measure performance
    (meanNumberOfSwaps,
     meanNumberOfComparisons) = algorithmPerformance()
    # Print results
    print(f"list-length: {N}, iterations: {ITERATIONS}")
    print(f"Mean number of swaps: {meanNumberOfSwaps}")
    print(f"Mean number of comparisons: {meanNumberOfComparisons}")

    # Sort and display once
    # Generate a list of random numbers
    myList = generateRandomList(MIN, MAX, N, verbose=False)
    # Sort the list and collect statistics
    (mySortedList,
     numberOfSwaps,
     numberOfComparisons) = bubbleSort(myList, verbose=False)

    if __debug__:
        print(f"in = {myList}")
        print(f"out = {mySortedList}")
