# coding: utf-8
"""
bubblesort 

Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
__all__ = ["bubbleSort", "bubbleSortVerbose"]

def bubbleSort(theList: list) -> tuple:
    """
    Sort a list of numbers in increasing order using bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made
    """
    theListCopy = theList + []
    done = False
    numberOfSwaps = 0
    numberOfComparisons = 0
    while not done:
        done = True
        for index in range(len(theListCopy) - 1):
            numberOfComparisons += 1
            if theListCopy[index] > theListCopy[index + 1]:
                done = False
                numberOfSwaps += 1
                (theListCopy[index],
                 theListCopy[index + 1]) = (theListCopy[index + 1],
                                            theListCopy[index])
    return (theListCopy, numberOfSwaps, numberOfComparisons)


def bubbleSortVerbose(theList: list) -> tuple:
    """Bubblesort"""
    theListCopy = theList + []
    done = False
    numberOfSwaps = 0
    numberOfComparisons = 0
    iteration = 1
    while not done:
        done = True
        print(f"iteration: {iteration}")
        for index in range(len(theListCopy) - 1):
            numberOfComparisons += 1
            print(f"index: {index}:")
            print(f"{theListCopy} ", end="")
            if theListCopy[index] > theListCopy[index + 1]:
                done = False
                numberOfSwaps += 1
                print(f"---> ({index} > {index + 1}) swapped  <--- {theListCopy}")
                (theListCopy[index],
                 theListCopy[index + 1]) = (theListCopy[index + 1],
                                            theListCopy[index])
            else:
                print(f"---> ({index} <= {index + 1}) no swap <--- {theListCopy}")
        print()
        iteration += 1

    print(f"Number of comparisons: {numberOfComparisons}")
    print(f"Number of swaps: {numberOfSwaps}")

    return (theListCopy, numberOfSwaps, numberOfComparisons)
