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
from algorithms.bubblesortplus import bubbleSortPlus
from algorithms.bubblesort import bubbleSort


def main() -> None:
    """Measure execution time, average number of comparisons
    and average number of swaps of bubbleSort() and
    bubbleSortPlus()"""

    # Initialise three lists used for collecting 
    # performance data of each run. Later used
    # (see below) for comparing the two algorithms.
    executionTimesCollected_bubbleSortPlus = []
    executionTimesCollected_bubbleSort = []

    averageComparisonsCollected = []
    averageSwapsCollected = []

    # Loop and collect data
    loopCount = 2
    for _ in range(loopCount):

        # Initialise three lists used for collecting
        # performance data of the algorithms. Later used
        # (see below) for comparing the two algorithms.
        executionTimes = []
        averageComparisons = []
        averageSwaps = []
    
        # Once for each algorithm, 
        # measure the performance
        for algorithm in (bubbleSortPlus, bubbleSort):
    
            sortAlgorithm = algorithm
            print(f"Measuring performance of {sortAlgorithm.__name__}")
            print(f"List-length: {N}")
            # Measure execution time
            print(f"Execution time (using the timeit module) "
                  f"({TIMEIT_ITERATIONS} iterations):")
            elapsed = timeIt(algorithm=sortAlgorithm)
            executionTimes.append(elapsed)
            print(f"Elapsed = %6.4f seconds ({TIMEIT_ITERATIONS} iterations)" % elapsed)
            # Measure performance in terms of (mean) number of
            # swaps and (mean) number of comparisons
            print(f"Number of comparisons "
                  f"and swaps ({ITERATIONS} iterations):")
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
            ## (sortedRandomNumbers, _, _) = bubbleSortPlus(randomNumbers)
            ## print(f"in = {randomNumbers}")
            ## print(f"out = {sortedRandomNumbers}")
    
    
        executionTimesCollected_bubbleSortPlus.append(
            executionTimes[0])
        executionTimesCollected_bubbleSort.append(
            executionTimes[1])
        print("= " * 40)
        print(f"Execution time ratio "
              "(bubbleSort / bubbleSortPlus): %6.4f" % 
              (executionTimes[1] / executionTimes[0]))
        print(f"Average number of comparisons ratio "
              "(bubbleSort / bubbleSortPlus): %6.4f" % 
              (averageComparisons[1] / averageComparisons[0]))
        print("Average number of swaps ratio "
              "(bubbleSort / bubbleSortPlus): %6.4f" % 
              (averageSwaps[1] / averageSwaps[0]))
        print("= " * 40)

    print("%6.4f" % (sum(executionTimesCollected_bubbleSortPlus) / loopCount))
    print("%6.4f" % (sum(executionTimesCollected_bubbleSort) / loopCount))

if __name__ == "__main__":
    main()
