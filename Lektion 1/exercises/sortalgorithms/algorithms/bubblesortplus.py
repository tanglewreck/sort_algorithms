# coding: utf-8

"""
    Sort a list of numbers in increasing order using
    a modified version of bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made
"""

__all__ = ["bubbleSortPlus", "bubbleSortPlusVerbose"]

# pylint: disable=invalid-name

#def switchPlace(theList: list, positionOne: int, positionTwo: int) -> None:
#    """
#    Utility function that swaps places of two elements.
#    The position of the elements are given by the (integer)
#    parameters 'positionOne' and 'positionTwo.
#
#    NOTE that using this function implies a performance hit
#    as  compared to doing the swap inline. The code is
#    preserved as a reminder of this.
#    """
#    try:
#        theList[positionOne], theList[positionTwo] = theList[positionTwo], theList[positionOne]
#    except IndexError as e:
#        print(f"Got an IndexError: {e}")


def bubbleSortPlus(theList: list, reverse = True) -> tuple:
    """
    foo
    """
    listLen: int = len(theList)

    numberOfComparisons = numberOfSwaps = 0

    listCopy = theList.copy()

    for indexOne, _ in enumerate(listCopy):  # outer loop
        done = True
        for indexTwo in range(indexOne + 1, listLen):  # inner loop
            numberOfComparisons += 1
            if listCopy[indexOne] > listCopy[indexTwo]:
                listCopy[indexOne], listCopy[indexTwo] = listCopy[indexTwo], listCopy[indexOne]
                numberOfSwaps += 1
                done = False
        if done:
            break

    if reverse:
        return (listCopy[::-1], numberOfSwaps, numberOfComparisons)
    return (listCopy, numberOfSwaps, numberOfComparisons)


def bubbleSortPlus2(theList: list, reverse = True) -> tuple:
    """
    This functions sorts a list of numbers using a modified version
    of bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made

    """
    # Store the length of the list in a variable, for easy access
    listLen: int = len(theList)

    # We count the number of comparisons and swaps made
    numberOfComparisons = 0
    numberOfSwaps = 0

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    listCopy = theList.copy()

    # Repeatedly iterate through the list of numbers, compare the first element with
    # the rest of the elements in turn, switching places if the first is larger
    # than the other element, thus forcing the smallest element of the list to
    # the head.
    #
    # Since, in each iteration, the smallest number is moved to the head of the
    # list in this way, we can optimise by ignoring those numbers we have
    # already moved.
    #
    # Another way of putting this is that the list elements that are moved to
    # the beginning of the list are all in their correct position, so we can ignore
    # those elements as we progress further down the list.

    # Forward sort
    # for indexOne in range(0, listLen):  # outer loop
    # for indexOne in range(len(listCopy)):  # outer loop
    for indexOne, _ in enumerate(listCopy):  # outer loop
        # If no swaps are made, we're done
        done = True
        for indexTwo in range(indexOne + 1, listLen):  # inner loop
            numberOfComparisons += 1
            if listCopy[indexOne] > listCopy[indexTwo]:
                # Make the swap
                listCopy[indexOne], listCopy[indexTwo] = listCopy[indexTwo], listCopy[indexOne]
                numberOfSwaps += 1
                done = False
        if done:
            break


    if reverse:
        return (listCopy[::-1], numberOfSwaps, numberOfComparisons)
    return (listCopy, numberOfSwaps, numberOfComparisons)


def bubbleSortPlusVerbose(theList: list) -> tuple:
    """
    Verbose, otherwise same as above
    """
    # Store the length of the list in a variable, for easy access
    listLen: int = len(theList)

    # We count the number of comparisons and swaps made
    numberOfComparisons = 0
    numberOfSwaps = 0

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    listCopy = theList + []

    # Repeatedly iterate through the list of numbers, compare the first element with
    # the rest of the elements in turn, switching places if the first is larger
    # than the other element, thus forcing the smallest element of the list to
    # the head.
    #
    # Since, in each iteration, the smallest number is moved to the head of the
    # list in this way, we can optimise by ignoring those numbers we have
    # already moved (the 'firstIndex' variable keeps track of this).
    #
    # Another way of putting this is that the list elements that are moved to
    # the beginning of the list are all in their correct position, so we can ignore
    # those elements as we progress further down the list.

    # The variable 'firstIndex' is incremented by one with each
    # iteration of the loop, making the list of numbers
    # to compare shorter for (almost) every run of the loop.
    firstIndex = 0

    for indexOne in range(firstIndex, listLen):
        print(f"interation: {indexOne} (firstIndex = {firstIndex})")
        for indexTwo in range(indexOne + 1, listLen):  # loop from indexOne to listLen -1
            print(f"{listCopy}\t", end="")

            numberOfComparisons += 1
            if listCopy[indexOne] > listCopy[indexTwo]:
                print(f"---> ({listCopy[indexOne]} > {listCopy[indexTwo]}) swapped  <--- ", end="")
                # Make the swap
                listCopy[indexOne], listCopy[indexTwo] = listCopy[indexTwo], listCopy[indexOne]
                numberOfSwaps += 1
            else:
                print(f"---> ({listCopy[indexOne]} <= {listCopy[indexTwo]}) no swap  <--- ", end="")
            print(listCopy)
        print()
        firstIndex += 1

    print(f"Number of comparisons: {numberOfComparisons}")
    print(f"Number of swaps: {numberOfSwaps}")

    return (listCopy, numberOfSwaps, numberOfComparisons)
