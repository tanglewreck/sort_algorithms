# coding: utf-8
import numpy as np
import timeit

# MIN = 1
# MAX = 10
# N = 10

# Number of numbers in the list
N = 100
# Min size of a number in the list
MIN = 1
# Max size of a number in the list
MAX = 1000

L = [int(x) for x in np.random.randint(MIN, MAX, N,dtype=int)]

def bubbleSort(theList: list = L, verbose = False):
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
    

def main():
    iterations = 100_000
    iterations = 10_000
    sumOfSwaps = 0
    sumOfComparisons = 0
    for k in range(iterations):
        intList = [int(x) for x in np.random.randint(MIN, MAX, N,dtype=int)]
        (intListSorted,
         numberOfSwaps,
         numberOfComparisons) = bubbleSort(intList)
        sumOfSwaps += numberOfSwaps
        sumOfComparisons += numberOfComparisons
        # print(numberOfSwaps)
        # print(numberOfComparisons)
        # print(intListSorted)
    print(f"list-length: {N}, iterations: {iterations}")
    print(f"Mean number of swaps: {sumOfSwaps / iterations}")
    print(f"Mean number of comparisons: {sumOfComparisons / iterations}")

if __name__ == "__main__":
    #t = timeit.Timer("main")
    #elapsed = t.timeit(100_000_000)
    #print(elapsed)
    (sortedList,
     numberOfSwaps,
     numberOfComparisons) = bubbleSort(L, verbose=False)
    #print(f"Number of swaps: {numberOfSwaps}")
    #print(f"Number of comparisons: {numberOfComparisons}")
    main()
