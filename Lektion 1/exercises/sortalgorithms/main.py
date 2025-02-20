"""
2025-02-19
sortalgorithms.py

Uses bubblesort and a modified version
of that algorithm to sort lists of numbers.

NOTE: run with '-O' to get rid of (excessive) output

"""
import numpy as np

from algorithms.performance import timeIt
from algorithms.performance import algorithmPerformance
from algorithms.defaults import N, MIN, MAX
from algorithms.defaults import ITERATIONS, TIMEIT_ITERATIONS
from algorithms.defaults import MEASUREMENTS
from algorithms.bubblesortplus import bubbleSortPlus
from algorithms.bubblesort import bubbleSort
# from algorithms.utils import generateRandomList


def main() -> None:
    """
    Measure execution time, mean number of comparisons
    and mean number of swaps of bubbleSort() and
    bubbleSortPlus()

    NOTE: This function is too long and contains too many local variables
          (according to pylint, at least)
    """

    # Initialise three lists used for collecting
    # performance data of each run. Later used
    # (see below) for comparing the two algorithms.
    executionTimeCollected_bubbleSortPlus = []
    executionTimeCollected_bubbleSort = []

    comparisonsCollected_bubbleSort = []
    comparisonsCollected_bubbleSortPlus = []

    swapsCollected_bubbleSort = []
    swapsCollected_bubbleSortPlus = []

    # Loop and collect data
    print("Measuring performance...")
    print(f"List-length: {N}")
    print(f"MIN: {MIN}")
    print(f"MAX: {MAX}")
    print(f"Number of iterations: {ITERATIONS}")
    print(f"Number of iterations (timeit): {TIMEIT_ITERATIONS}")
    print(f"Number of measurements: {MEASUREMENTS}")
    for _ in range(MEASUREMENTS):

        # Initialise three lists used for collecting
        # performance data of the algorithms. Later used
        # (see below) for comparing the two algorithms.
        executionTimes = []
        meanComparisons = []
        meanSwaps = []

        # Once for each algorithm,
        # measure the performance
        for sortAlgorithm in (bubbleSortPlus, bubbleSort):

            if __debug__:
                print(f"Measuring performance of {sortAlgorithm.__name__}")
                print(f"List-length: {N}")
                print(f"Execution time (using the timeit module) "
                      f"({TIMEIT_ITERATIONS} iterations):")
            # Measure execution time
            elapsed = timeIt(algorithm=sortAlgorithm)
            executionTimes.append(elapsed)
            if __debug__:
                print(f"Elapsed = %6.4f seconds ({TIMEIT_ITERATIONS} iterations)" % elapsed)
                print(f"Number of comparisons "
                      f"and swaps ({ITERATIONS} iterations):")
            # Measure performance in terms of (mean) number of
            # swaps and (mean) number of comparisons
            (meanNumberOfSwaps,
             meanNumberOfComparisons) = algorithmPerformance(
                                                iterations=ITERATIONS,
                                                func=sortAlgorithm
            )
            if __debug__:
                print(f"mean number of swaps: {meanNumberOfSwaps:6.4f}")
                print(f"mean number of comparisons: {meanNumberOfComparisons}")
                print("Done.")
                print("")

            meanComparisons.append(meanNumberOfComparisons)
            meanSwaps.append(meanNumberOfSwaps)


        # Add data to overall statistics
        executionTimeCollected_bubbleSortPlus.append(
            executionTimes[0])
        executionTimeCollected_bubbleSort.append(
            executionTimes[1])

        comparisonsCollected_bubbleSortPlus.append(
            meanComparisons[0])
        comparisonsCollected_bubbleSort.append(
            meanComparisons[1])

        swapsCollected_bubbleSortPlus.append(
            meanSwaps[0])
        swapsCollected_bubbleSort.append(
            meanSwaps[1])

        if __debug__:
            print("= " * 40)
            print("Execution time ratio "
                  f"(bubbleSort / bubbleSortPlus): {
                        (executionTimes[1] / executionTimes[0]):2.2f
                  }")
            print(f"mean number of comparisons ratio "
                  f"(bubbleSort / bubbleSortPlus): {
                        (meanComparisons[1] / meanComparisons[0]):2.2f}")
            print("mean number of swaps ratio "
                  f"(bubbleSort / bubbleSortPlus): {
                        (meanSwaps[1] / meanSwaps[0]):2.2f}")
            print("= " * 40)


    #
    # Compute statistics (mean and standard deviation)
    #
    #   Execution time
    meanExecutionTime_bubbleSort = np.mean(executionTimeCollected_bubbleSort)
    meanExecutionTime_bubbleSortPlus = np.mean(executionTimeCollected_bubbleSortPlus)
    stddevExecutionTime_bubbleSort = np.sqrt(np.var(executionTimeCollected_bubbleSort))
    stddevExecutionTime_bubbleSortPlus = np.sqrt(np.var(executionTimeCollected_bubbleSortPlus))

    #   Comparisons
    meanComparisons_bubbleSort = np.mean(comparisonsCollected_bubbleSort)
    meanComparisons_bubbleSortPlus = np.mean(comparisonsCollected_bubbleSortPlus)
    stddevComparisons_bubbleSort = np.sqrt(np.var(comparisonsCollected_bubbleSort))
    stddevComparisons_bubbleSortPlus = np.sqrt(np.var(comparisonsCollected_bubbleSortPlus))

    #   Swaps
    meanSwaps_bubbleSort = np.mean(swapsCollected_bubbleSort)
    meanSwaps_bubbleSortPlus = np.mean(swapsCollected_bubbleSortPlus)
    stddevSwaps_bubbleSort = np.sqrt(np.var(swapsCollected_bubbleSort))
    stddevSwaps_bubbleSortPlus = np.sqrt(np.var(swapsCollected_bubbleSortPlus))

    print("\n", "= " * 40, "\n",
          f"Overall performance ({MEASUREMENTS} measurements):\n",
          "= " * 40)

    print(f"bubbleSort: {meanExecutionTime_bubbleSort:2.2f} ± "
          f"{stddevExecutionTime_bubbleSort:-2.2f} seconds")
    print(f"bubbleSortPlus: {meanExecutionTime_bubbleSortPlus:2.2f} ± "
          f"{stddevExecutionTime_bubbleSortPlus:-2.2f} seconds")
    print(f"ratio: {(meanExecutionTime_bubbleSort /
                     meanExecutionTime_bubbleSortPlus):2.2f}")

    print(f"\nbubbleSort: {meanComparisons_bubbleSort:2.2f} ± "
          f"{stddevComparisons_bubbleSort:2.2f} comparisons")
    print(f"bubbleSortPlus: {meanComparisons_bubbleSortPlus:2.2f} ± "
          f"{stddevComparisons_bubbleSortPlus:2.2f} comparisons")
    print(f"ratio: {(meanComparisons_bubbleSort /
                     meanComparisons_bubbleSortPlus ):2.2f}")

    print(f"\nbubbleSort: {meanSwaps_bubbleSort:2.2f} ± "
          f"{stddevSwaps_bubbleSort:2.2f} swaps")
    print(f"bubbleSortPlus: {meanSwaps_bubbleSortPlus:2.2f} ± "
          f"{stddevSwaps_bubbleSortPlus:2.2f} swaps")
    print(f"ratio: {(meanSwaps_bubbleSort /
                    meanSwaps_bubbleSortPlus):2.2f}")
    print("= " * 40)


#    # Sort and display once to make verify that the algorithm works
#    randomNumbers = generateRandomList(MIN, MAX, N)
#    # Sort the list and collect statistics
#    (sortedRandomNumbers, _, _) = bubbleSortPlus(randomNumbers)
#    print(f"in = {randomNumbers}")
#    print(f"out = {sortedRandomNumbers}")


if __name__ == "__main__":
    main()
