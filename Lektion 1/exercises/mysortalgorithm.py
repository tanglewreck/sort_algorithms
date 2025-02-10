# coding: utf-8

"""
mySortAlgorithm-sort a random list of ints in increasing order.
Uses numpy to generate a list of N integers.
Run with '-O' to get rid of debug messages.
Comes with rudimentary commandline argument handling (using sys.argv)
NOTE: camelCase variable-names in use :)

pylint:
pylint --function-naming-style camelCase \
       --variable-naming-style camelCase \
       --argument-naming-style cameCase mysortalgorithm.py

"""

import sys
import textwrap
# import timeit

import numpy as np

# Number of numbers in the list
N = 100
# Min size of a number in the list
MIN = 1
# Max size of a number in the list
MAX = 1000


def getCommandLineArguments() -> list:
    """
    Get commandline arguments using sys.argv.
    """

    USAGE = f"{sys.argv[0]} <minimum> <maximum> <list-length>"
    # Assign default values
    minimum = MIN
    maximum = MAX
    numbersToGenerate = N

    try:
        if len(sys.argv) == 1:
            (minimum,
             maximum,
             numbersToGenerate) = (MIN, MAX, N)
        elif len(sys.argv) == 2:
            # One commandline argument
            minimum = int(sys.argv[1])
        elif len(sys.argv) == 3:
            # Two commandline arguments
            (minimum,
             maximum)  = [int(x) for x in sys.argv[1:]]
        elif len(sys.argv) == 4:
            # Three commandline arguments
            (minimum,
             maximum,
             numbersToGenerate)  = [int(x) for x in sys.argv[1:]]
    except ValueError as e:
        print(f"Got a ValueError: {e}", file=sys.stderr)
        raise SystemExit(1) from e

    # Sanity checks
    if maximum < minimum:
        print(textwrap.dedent(f"""
              WARNING: Maximum must be larger than minimum.
              Switched order of arguments.
              Usage: {USAGE}
        """))
        (minimum, maximum) = (maximum, minimum)
    if (maximum - minimum ) < numbersToGenerate - 1:
        print(f"Distance between minimum ({minimum}) and maximum ({maximum}) "
               "is less than the numbers of numbers to "
               f"generate (default: {N}).")
        raise SystemExit(1)

    if __debug__:
        print(f"min, max, numbersToGenerate = {minimum}, {maximum}, {numbersToGenerate}")

    return (minimum, maximum, numbersToGenerate)


def generateRandomNumbers(minimum = MIN, maximum = MAX,
                          numbersToGenerate = N,
                          verbose=False) -> list:
    """
    Generate random integers btw min (inclusive) and max (inclusive).
    """
    try:
        randomList = [int(n) for n in np.random.choice(range(minimum, maximum + 1),
                                      size=numbersToGenerate,
                                      replace=False)]
        if verbose:
            print(randomList)
        return randomList

    except ValueError as e:
        print(e)
        raise SystemExit(1) from e


def mySortAlgorithm(theList: list, verbose = False):
    """
    This functions sorts a list of numbers using a modified version
    of bubblesort (??) 
    """

    def switchPlace(theList: list, positionOne: int, positionTwo: int) -> None:
        """
        Utility function that swaps places of two elements.
        The position of the elements are given by the (integer)
        parameters 'positionOne' and 'positionTwo.
        """
        try:
            theList[positionOne], theList[positionTwo] = theList[positionTwo], theList[positionOne]
        except IndexError as e:
            print(f"Got an IndexError: {e}")



    # Store the length of the list in a variable, for easy access
    listLen: int = len(theList)

    # We count the number of comparisons and swaps made
    numberOfComparisons = 0
    numberOfSwaps = 0

    saveList = theList + []
    # Loop through the list, twice, and switch elements as necessary
    # After each (outer) iteration, another least element will have been
    # added at the front of the list, which means we do not have to
    # consider those elements as we move along the list.
    # Another way of putting this is that the list elements that are put at the
    # beginning of the list are in their correct position, so we can ignore
    # those elements as we progress further down the list.

    firstIndex = 0  # Position of the first unsorted element
    for indexOne in range(firstIndex, listLen):
        # The variable 'firstIndex' is incremented by 1 with each
        # iteration of the loop, making the list of numbers
        # to compare monotonically shorter.
        if verbose:
            print(f"interation: {indexOne} (firstIndex = {firstIndex})")
            # print(saveList, saveList)

        for indexTwo in range(indexOne + 1, listLen):  # loop from indexOne to listLen -1
            # saveList = theList + []  # Don't remember how to deep-copy a list
            if verbose:
                print(f"{saveList}\t", end="")
            # if verbose:
            #    print(f"indices: ({indexOne, indexTwo})")

            numberOfComparisons += 1
            if saveList[indexOne] > saveList[indexTwo]:
                numberOfSwaps += 1
                switchPlace(saveList, indexOne, indexTwo)
                if verbose:
                    print("---> swapped <---\t", end="")
            else:
                if verbose:
                    print("---> no swap <---\t", end="")
            if verbose:
                print(saveList)
        if verbose:
            print()
        firstIndex += 1
    if verbose:
        print(f"Number of comparisons: {numberOfComparisons}")
        print(f"Number of swaps: {numberOfSwaps}")
    return (saveList, numberOfSwaps, numberOfComparisons)


def main():
    """ main  """
    # Get commandline arguments (minimum, maximum, number numbers to generate)
    (minimum, maximum, numbersToGenerate) = getCommandLineArguments()
    
    # Generate a list of random numbers
    myList = generateRandomNumbers(minimum, maximum, numbersToGenerate, verbose=False)
    mySortedList, numberOfSwaps, numberOfComparisons = mySortAlgorithm(myList, verbose=False)
    if __debug__:
        print(f"in = {myList}")
        print(f"out = {mySortedList}")

    iterations = 100_000
    iterations = 10_000
    sumOfSwaps = 0
    sumOfComparisons = 0
    for k in range(iterations):
        intList = generateRandomNumbers(minimum, maximum, numbersToGenerate)
        (intListSorted, numberOfSwaps, numberOfComparisons) = mySortAlgorithm(intList)
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons
        # print(numberOfSwaps)
        # print(numberOfComparisons)
        # print(intListSorted)
    print(f"list-length: {numbersToGenerate}, iterations: {iterations}")
    print(f"Mean number of swaps: {sumOfSwaps / iterations}")
    print(f"Mean number of comparisons: {sumOfComparisons / iterations}")


if __name__ == "__main__":
    # Time main() (no output generated)
    # iterations = 100_000_000
    # t = timeit.Timer(stmt="main")
    # try:
    #     elapsed = t.timeit(iterations)
    #     print(f"elapsed = {elapsed} ({iterations} iterations)")
    # except:
    #     print("EEEEEERRROR")
    # Run main once again (generates output)
    main()
