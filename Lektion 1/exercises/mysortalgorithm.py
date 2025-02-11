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
import timeit

import numpy as np

# Default values
#
# Number of numbers in the list
N = 100
# Min size of a number in the list
MIN = 1
# Max size of a number in the list
MAX = 1000
# Number of iterations while measuring performance
ITERATIONS = 10_000


def getCommandLineArguments(minimum: int = MIN,
                            maximum: int = MAX,
                            numbersToGenerate: int = N) -> list:
    """
    Get commandline arguments using sys.argv (instead of using the 
    argparse module).

    First argument: minimum (smallest integer to generate)
    Second argument: maximum (largest integer to generate)
    Third argument: number of integers to generate (=list-length)

    """

    try:
        if len(sys.argv) == 1:
            # No commandline arguments
            (minimum,
             maximum,
             numbersToGenerate) = (MIN, MAX, N)
        elif len(sys.argv) == 2:
            # One commandline argument
            minimum = int(sys.argv[1])
        elif len(sys.argv) == 3:
            # Two commandline arguments
            (minimum,
             maximum)  = [int(arg) for arg in sys.argv[1:]]
        elif len(sys.argv) == 4:
            # Three commandline arguments
            (minimum,
             maximum,
             numbersToGenerate)  = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        print(f"Got a ValueError: {e}", file=sys.stderr)
        raise SystemExit(1) from e

    # Sanity checks
    if maximum < minimum:
        print(textwrap.dedent(f"""
              WARNING: Maximum must be larger than minimum.
              Switching order.
              Usage: {USAGE}
        """))
        (minimum, maximum) = (maximum, minimum)
    if (maximum - minimum ) < (numbersToGenerate - 1):
        print(f"Distance between minimum ({minimum}) and maximum ({maximum}) "
               "is less than the numbers of numbers to "
               f"generate (default: {N}).")
        raise SystemExit(1)

    if __debug__:
        print(f"min, max, numbersToGenerate = {minimum}, {maximum}, {numbersToGenerate}")

    return (minimum, maximum, numbersToGenerate)


def generateRandomList(minimum: int = MIN,
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

        NOTE that using this function implies a performance hit 
        compared to doing the swap inline.
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
    # to compare monotonically shorter for each run of the loop.
    firstIndex = 0  

    for indexOne in range(firstIndex, listLen):
        if verbose:
            print(f"interation: {indexOne} (firstIndex = {firstIndex})")

        for indexTwo in range(indexOne + 1, listLen):  # loop from indexOne to listLen -1
            if verbose:
                print(f"{listCopy}\t", end="")

            numberOfComparisons += 1
            if listCopy[indexOne] > listCopy[indexTwo]:
                # Make the swap
                # switchPlace(listCopy, indexOne, indexTwo)
                listCopy[indexOne], listCopy[indexTwo] = listCopy[indexTwo], listCopy[indexOne]
                numberOfSwaps += 1
                if verbose:
                    print("---> swapped <---\t", end="")
            else:
                if verbose:
                    print("---> no swap <---\t", end="")
            if verbose:
                print(listCopy)
        if verbose:
            print()
        firstIndex += 1

    if verbose:
        print(f"Number of comparisons: {numberOfComparisons}")
        print(f"Number of swaps: {numberOfSwaps}")

    return (listCopy, numberOfSwaps, numberOfComparisons)


def algorithmPerformance(iterations: int = ITERATIONS) -> tuple:
    """Simple performance test of the sorting
    algorithm, using the average number of swaps 
    and comparisons over a large number of runs as
    indicators of efficiency."""

    sumOfSwaps = 0
    sumOfComparisons = 0
    for k in range(iterations):
        # Generate a random list
        intList = generateRandomList(minimum,
                                     maximum,
                                     numbersToGenerate)
        # Sort the list
        (intListSorted,
         numberOfSwaps,
         numberOfComparisons) = mySortAlgorithm(intList, verbose=False)

        # Update sums
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons

    meanNumberOfSwaps = sumOfSwaps / iterations
    meanNumberOfComparisons = sumOfComparisons / iterations 

    return (meanNumberOfSwaps, meanNumberOfComparisons)


def main(minimum: MIN, maximum: MAX, numbersToGenerate: N):
    """ main  """
    # Generate a list of random numbers
    myList = generateRandomList(minimum,
                                maximum,
                                numbersToGenerate,
                                verbose=False)
    # Sort the list and collect statistics
    (mySortedList,
     numberOfSwaps,
     numberOfComparisons) = mySortAlgorithm(myList, verbose=False)
    

if __name__ == "__main__":
    # Get commandline arguments (minimum, maximum, number numbers to generate)
    (minimum,
     maximum,
     numbersToGenerate) = getCommandLineArguments()
    
    # Use the timeit module to measure performance
    # Time main() (no output generated)
    iterations = 100_000_000
    t = timeit.Timer(stmt="main")
    try:
        elapsed = t.timeit(iterations)
        print(f"elapsed = {elapsed} ({iterations} iterations)")
    except:
        print("EEEEEERRROR")


    # Measure performance
    (meanNumberOfSwaps,
     meanNumberOfComparisons) = algorithmPerformance()
    # Print results
    print(f"list-length: {numbersToGenerate}, iterations: {ITERATIONS}")
    print(f"Mean number of swaps: {meanNumberOfSwaps}")
    print(f"Mean number of comparisons: {meanNumberOfComparisons}")

    # Sort and display once
    # Generate a list of random numbers
    myList = generateRandomList(minimum,
                                maximum,
                                numbersToGenerate,
                                verbose=False)
    # Sort the list and collect statistics
    (mySortedList,
     numberOfSwaps,
     numberOfComparisons) = mySortAlgorithm(myList, verbose=False)

    if __debug__:
        print(f"in = {myList}")
        print(f"out = {mySortedList}")
