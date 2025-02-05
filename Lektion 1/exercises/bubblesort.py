# coding: utf-8

"""
Bubblesort a random list of ints in increasing order.
Uses numpy to generate a list of N integers.
Run with '-O' to get rid of debug messages.
Comes with rudimentary commandline argument handling (using sys.argv)
NOTE: camelcase variable-names in use :) 
"""

import numpy as np
import sys

N = 10     # Number of numbers in the list
MIN = 1    # Min size of a number in the list
MAX = 100  # Max size of a number in the list


def generateRandomNumbers(min = MIN, max = MAX, numbersToGenerate = N) -> list:
    """
    Generate random integers btw min (inclusive) and max (inclusive).
    """
    try:
        return [int(n) for n in
                        np.random.choice(range(min, max + 1),
                                         size=numbersToGenerate,
                                         replace=False)
                ]
    except ValueError as e:
        print(e)
        raise SystemExit(1)


def bubbleSort(theList: list):
    """
    This functions sorts a list of numbers using bubblesort
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



    # Store the lenght of the list in a variable 
    listLen: int = len(theList)

    saveList = theList + [0]
    # Loop through the list, twice, and switch elements as necessary
    for indexOne in range(listLen):  # loop from 0 to listLen - 1
        if __debug__:
            print(f"interation: {indexOne}")
            # print(saveList, theList)

        for indexTwo in range(indexOne + 1, listLen):  # loop from indexOne to listLen -1
            saveList = theList + [0]  # Don't remember how to deep-copy a list
            saveList.pop()            # so this will have to do.
            if __debug__:
                print(f"{saveList}\t", end="")
            # if __debug__:
            #    print(f"indices: ({indexOne, indexTwo})")

            if theList[indexOne] > theList[indexTwo]:
                # if __debug__:
                # print(f"switching: ({indexOne, indexTwo})\t({theList[indexOne], theList[indexTwo]})")
                switchPlace(theList, indexOne, indexTwo)
                if __debug__:
                    print("---> swapped <---\t", end="")
            else:
                if __debug__:
                    print("---> no swap <---\t", end="")
            if __debug__:
                print(theList)
        if __debug__:
            print()

def getCommandLineArguments() -> list:
    """
    Get commandline arguments using sys.argv.
    """
    # Assign default values 
    min = MIN
    max = MAX
    numbersToGenerate = N

    # Check if there's a first argument
    try:
        if sys.argv[1]:
            errorMessage = "Input must be integers"
            try:
                min: int = int(sys.argv[1])
                if __debug__:
                    print(f"Assigned min ({min})")
            except ValueError as e:
                print(f"{errorMessage}: {e}", file=sys.stderr)
                raise
        
        # Check if there's a second argument
        try:
            if sys.argv[2]:
                try:
                    max: int = int(sys.argv[2])
                    if __debug__:
                        print(f"Assigned max ({max})")
                except ValueError as e:
                    print(f"{errorMessage}: {e}", file=sys.stderr)
                    raise SystemExit(1)

            # Check if there's a third argument
            try:
                if sys.argv[3]:
                    try:
                        numbersToGenerate: int = int(sys.argv[3])
                    except ValueError as e:
                        print(f"{errorMessage}: {e}", file=sys.stderr)
                        raise SystemExit(1)
                else:
                    numbersToGenerate = N
            except IndexError:
                # Third argument is absent – nothing to do
                print("no third argument")
                pass

        except IndexError:
            # Second argument is absent (and, then, so is the third); assign default values
            print("assigned default value to max")
            max = MAX
    
    except IndexError:
        # First argument is absent (and so are the second and third); assign default values
        print("assigned default value to min")
        min = MIN

    # Sanity check
    if max < min:
        raise SystemExit(1, "max must be larger than min")

    if __debug__:
        print(f"min, max, numbersToGenerate = {min}, {max}, {numbersToGenerate}")

    return (min, max, numbersToGenerate)



def main():

    (min, max, numbersToGenerate) = getCommandLineArguments()

    # Generate a list of random numbers 
    myList = generateRandomNumbers(min, max, numbersToGenerate)
    #if __debug__:
    #    print(f"in = {myList}")
    #    print()

    # Sort the list and print the result
    # myList = [72, 37, 4, 17, 9]
    bubbleSort(myList)
    print(f"out = {myList}")

if __name__ == "__main__":
    main()
