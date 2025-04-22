# coding: utf-8
"""
bubblesort 

Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
# pylint: disable=invalid-name
# pylint: disable=too-many-locals
# pylint: disable=consider-using-enumerate
### pylint: disable=too-many-statements

__all__ = ["bubbleSort",
           "bubbleSort2",
           "bubbleSort3",
           "bubbleSortVerbose"]

def bubbleSort(theList: list) -> tuple:
    """
    Sort a list of numbers in increasing order using bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made
    """
    listCopy = theList.copy()
    done = False
    numberOfSwaps = 0
    numberOfComparisons = 0
    while not done:
        done = True
        for index in range(len(listCopy) - 1):
            numberOfComparisons += 1
            if listCopy[index] > listCopy[index + 1]:
                done = False
                numberOfSwaps += 1
                (listCopy[index],
                 listCopy[index + 1]) = (listCopy[index + 1],
                                            listCopy[index])
    return (listCopy, numberOfSwaps, numberOfComparisons)


def bubbleSort2_2(theList: list) -> tuple:
    """
    Sort a list of numbers in increasing order using bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made
    """
    listCopy = theList.copy()
    done = False
    numberOfSwaps = 0
    numberOfComparisons = 0
    while not done:
        done = True
        for index in range(len(listCopy) - 1):
            numberOfComparisons += 1
            if listCopy[index] > listCopy[index + 1]:
                done = False
                numberOfSwaps += 1
                (listCopy[index],
                 listCopy[index + 1]) = (listCopy[index + 1],
                                            listCopy[index])
    return (listCopy, numberOfSwaps, numberOfComparisons)


def bubbleSort2(theList: list) -> tuple:
    """Another bubblesort implementation"""
    listCopy = theList.copy()
    numberOfSwaps = 0
    numberOfComparisons = 0
    for _ in range(len(listCopy)):
        for index in range(len(listCopy) - 1):
            numberOfComparisons += 1
            if listCopy[index] > listCopy[index + 1]:
                numberOfSwaps += 1
                (listCopy[index],
                 listCopy[index + 1]) = (listCopy[index + 1],
                                      listCopy[index])
    return (listCopy, numberOfSwaps, numberOfComparisons)


def bubbleSort3(theList: list) -> tuple:
    """Another bubblesort implementation"""
    listCopy = theList.copy()
    numberOfSwaps = 0
    numberOfComparisons = 0
    for index1 in range(len(listCopy)):
        for index2 in range(len(listCopy) - 1):
            numberOfComparisons += 1
            if listCopy[index1] > listCopy[index2]:
                numberOfSwaps += 1
                (listCopy[index1],
                 listCopy[index2]) = (listCopy[index2],
                                      listCopy[index1])
    return (listCopy, numberOfSwaps, numberOfComparisons)


def bubbleSortVerbose(theList: list) -> tuple:
    """Bubblesort"""
    listCopy = theList + []
    done = False
    numberOfSwaps = 0
    numberOfComparisons = 0
    iteration = 1
    while not done:
        done = True
        print(f"iteration: {iteration}")
        for index in range(len(listCopy) - 1):
            numberOfComparisons += 1
            print(f"index: {index}:")
            print(f"{listCopy} ", end="")
            if listCopy[index] > listCopy[index + 1]:
                done = False
                numberOfSwaps += 1
                print(f"---> ({index} > {index + 1}) swapped  <--- {listCopy}")
                (listCopy[index],
                 listCopy[index + 1]) = (listCopy[index + 1],
                                            listCopy[index])
            else:
                print(f"---> ({index} <= {index + 1}) no swap <--- {listCopy}")
        print()
        iteration += 1

    print(f"Number of comparisons: {numberOfComparisons}")
    print(f"Number of swaps: {numberOfSwaps}")

    return (listCopy, numberOfSwaps, numberOfComparisons)
