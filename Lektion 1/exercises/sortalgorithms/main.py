"""
2025-02-19
sortalgorithms.py

Uses bubblesort and a modified version
of that algorithm to sort lists of numbers.
"""

from algorithms.performance import timeIt
from algorithms.performance import algorithmPerformance
from algorithms.defaults import N, MIN, MAX
from algorithms.defaults import ITERATIONS, TIMEIT_ITERATIONS
from algorithms.mysortalgorithm import mySortAlgorithm
from algorithms.bubblesort import bubbleSort


def main() -> None:
    """main"""

    executionTimes = []
    averageComparisons = []
    averageSwaps = []
    for func in (mySortAlgorithm, bubbleSort):
        # Measure performance of mySortAlgorithm
        sortAlgorithm = func
        print(f"Measuring performance of {sortAlgorithm.__name__}")
        print(f"List-length: {N}")
        # Measure execution time
        print(f"Execution time using the timeit module "
              f"({TIMEIT_ITERATIONS} iterations):")
        elapsed = timeIt(func=sortAlgorithm)
        executionTimes.append(elapsed)
        print(f"Elapsed = %6.4f seconds ({TIMEIT_ITERATIONS} iterations)" % elapsed)
        # Measure performance in terms of (mean) number of
        # swaps and (mean) number of comparisons
        print(f"Performance in terms of number of comparisons "
              f"and number of swaps ({ITERATIONS} iterations):")
        (averageNumberOfSwaps,
         averageNumberOfComparisons) = algorithmPerformance(
                                            iterations=ITERATIONS,
                                            func=sortAlgorithm
        )
        # Print results
        print(f"Average number of swaps: %6.4f" % averageNumberOfSwaps)
        print(f"Average number of comparisons: {averageNumberOfComparisons}")
        print("Done.")
        print("")
    
        averageComparisons.append(averageNumberOfComparisons)
        averageSwaps.append(averageNumberOfSwaps)
        # Sort and display once to make verify that the algorithm works
        ## randomNumbers = generateRandomList(MIN, MAX, N)
        # Sort the list and collect statistics
        ## (sortedRandomNumbers, _, _) = mySortAlgorithm(randomNumbers)
        ## print(f"in = {randomNumbers}")
        ## print(f"out = {sortedRandomNumbers}")


    print("= " * 40)
    print(f"Execution time quotient "
          "(bubbleSort / mySortAlgorithm): %6.4f" % 
          (executionTimes[1] / executionTimes[0]))
    print(f"Average number of comparisons quotient "
          "(bubbleSort / mySortAlgorithm): %6.4f" % 
          (averageComparisons[1] / averageComparisons[0]))
    print("Average number of swaps quotient "
          "(bubbleSort / mySortAlgorithm): %6.4f" % 
          (averageSwaps[1] / averageSwaps[0]))
    print("= " * 40)

if __name__ == "__main__":
    main()
