#!/usr/bin/env python

"""
2025-02-19
sortalgorithms.py

Uses bubblesort and a modified version
of that algorithm to sort lists of numbers.

NOTE: run with '-O' to get rid of (excessive) output

"""

# pylint: disable=invalid-name
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=unused-import
#
import numpy as np
import matplotlib.pyplot as plt

from algorithms.performance import timeIt
from algorithms.performance import algorithmPerformance
from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTH, LIST_LENGTHS
from algorithms.defaults import MIN, MAX
from algorithms.defaults import ITERATIONS, TIMEIT_ITERATIONS
from algorithms.defaults import MEASUREMENTS
from algorithms.bubblesortplus import bubbleSortPlus
from algorithms.bubblesort import bubbleSort
from algorithms.bubblesort import bubbleSort2
from algorithms.bubblesort import bubbleSort3
# from algorithms.utils import generateRandomList

# LIST_LENGTHS = np.array([2, 5])
# LIST_LENGTHS = np.append(LIST_LENGTHS, np.arange(10, 100, 10))


def main() -> None:
    """
    Measure execution time, mean number of comparisons
    and mean number of swaps of bubbleSort() and
    bubbleSort2()

    NOTE: This function is too long and contains too many local variables
          (according to pylint, at least)
    """

    # Helper function
    def measurements(NumberOfMeasurements = MEASUREMENTS,
                     listLength = LIST_LENGTH):
        for _ in range(NumberOfMeasurements):
            # Initialise three lists used for collecting
            # performance data of the algorithms. Later used
            # (see below) for comparing the two algorithms.
            executionTimes = []
            meanComparisons = []
            meanSwaps = []

            # Once for each algorithm,
            # measure the performance
            for sortAlgorithm in (bubbleSort2, bubbleSort):
                # Measure execution time
                elapsed = timeIt(algorithm=sortAlgorithm,
                                 listLength=listLength)
                executionTimes.append(elapsed)
                # Measure performance in terms of (mean) number of
                # swaps and (mean) number of comparisons
                (meanNumberOfSwaps,
                 meanNumberOfComparisons) = algorithmPerformance(
                                                    iterations=ITERATIONS,
                                                    algorithm=sortAlgorithm,
                                                    listLength=listLength)
                meanComparisons.append(meanNumberOfComparisons)
                meanSwaps.append(meanNumberOfSwaps)

            # Add data to overall statistics
            executionTimeCollected_bubbleSort2.append(
                executionTimes[0])
            executionTimeCollected_bubbleSort.append(
                executionTimes[1])

            comparisonsCollected_bubbleSort2.append(
                meanComparisons[0])
            comparisonsCollected_bubbleSort.append(
                meanComparisons[1])

            swapsCollected_bubbleSort2.append(
                meanSwaps[0])
            swapsCollected_bubbleSort.append(
                meanSwaps[1])



    # main()
    print(f"LIST_LENGTHS: {LIST_LENGTHS}")
    print(f"""Measuring performance...
LIST_LENGTHS: {LIST_LENGTHS}
Min: {MIN}
Max: {MAX}
Number of iterations: {ITERATIONS}
Number of iterations (timeit): {TIMEIT_ITERATIONS}
Number of measurements: {MEASUREMENTS}""")
    # 'plot' arrays
    exe_bubbleSort = []
    exe_bubbleSort2 = []
    comp_bubbleSort = []
    comp_bubbleSort2 = []
    swaps_bubbleSort = []
    swaps_bubbleSort2 = []
    # Do measurements
    for listLength in LIST_LENGTHS:
        # Initialise three lists used for collecting
        # performance data of each run. Later used
        # (see below) for comparing the two algorithms.
        executionTimeCollected_bubbleSort2 = []
        executionTimeCollected_bubbleSort = []

        comparisonsCollected_bubbleSort = []
        comparisonsCollected_bubbleSort2 = []

        swapsCollected_bubbleSort = []
        swapsCollected_bubbleSort2 = []

        # Collect data
        print("\n", "-" * 40, sep="")
        print("listLength =", listLength, "\n")
        measurements(NumberOfMeasurements=MEASUREMENTS,
                     listLength=listLength)

        #
        # Compute statistics (mean and standard deviation)
        #
        #   Execution time
        meanExecutionTime_bubbleSort = np.mean(executionTimeCollected_bubbleSort)
        meanExecutionTime_bubbleSort2 = np.mean(executionTimeCollected_bubbleSort2)
        stddevExecutionTime_bubbleSort = np.sqrt(
                np.var(executionTimeCollected_bubbleSort))
        stddevExecutionTime_bubbleSort2 = np.sqrt(
                np.var(executionTimeCollected_bubbleSort2))

        #   Comparisons
        meanComparisons_bubbleSort = np.mean(comparisonsCollected_bubbleSort)
        meanComparisons_bubbleSort2 = np.mean(comparisonsCollected_bubbleSort2)
        stddevComparisons_bubbleSort = np.sqrt(
                np.var(comparisonsCollected_bubbleSort))
        stddevComparisons_bubbleSort2 = np.sqrt(
                np.var(comparisonsCollected_bubbleSort2))

        #   Swaps
        meanSwaps_bubbleSort = np.mean(swapsCollected_bubbleSort)
        meanSwaps_bubbleSort2 = np.mean(swapsCollected_bubbleSort2)
        stddevSwaps_bubbleSort = np.sqrt(
                np.var(swapsCollected_bubbleSort))
        stddevSwaps_bubbleSort2 = np.sqrt(
                np.var(swapsCollected_bubbleSort2))

        # Save mean values to 'plot' arrays
        exe_bubbleSort.append(meanExecutionTime_bubbleSort)
        exe_bubbleSort2.append(meanExecutionTime_bubbleSort2)
        comp_bubbleSort.append(meanComparisons_bubbleSort)
        comp_bubbleSort2.append(meanComparisons_bubbleSort2)
        swaps_bubbleSort.append(meanSwaps_bubbleSort)
        swaps_bubbleSort2.append(meanSwaps_bubbleSort2)
        #print("-" * 40, "\n",
        #      f"Performance ({MEASUREMENTS} measurements):\n",
        #      "-" * 40, sep="")

        print(f"bubbleSort: {meanExecutionTime_bubbleSort:2.3f} ± "
              f"{stddevExecutionTime_bubbleSort:-2.3f} seconds")
        print(f"bubbleSort2: {meanExecutionTime_bubbleSort2:2.3f} ± "
              f"{stddevExecutionTime_bubbleSort2:-2.3f} seconds")
        print(f"ratio: {(meanExecutionTime_bubbleSort /
                         meanExecutionTime_bubbleSort2):2.3f}")

        print(f"\nbubbleSort: {meanComparisons_bubbleSort:2.3f} ± "
              f"{stddevComparisons_bubbleSort:2.3f} comparisons")
        # print(f"{comparisonsCollected_bubbleSort}")

        print(f"bubbleSort2: {meanComparisons_bubbleSort2:2.3f} ± "
              f"{stddevComparisons_bubbleSort2:2.3f} comparisons")
        # print(f"{comparisonsCollected_bubbleSort2}")
        print(f"ratio: {(meanComparisons_bubbleSort /
                         meanComparisons_bubbleSort2 ):2.3f}")

        print(f"\nbubbleSort: {meanSwaps_bubbleSort:2.3f} ± "
              f"{stddevSwaps_bubbleSort:2.3f} swaps")
        # print(f"{swapsCollected_bubbleSort}")
        print(f"bubbleSort2: {meanSwaps_bubbleSort2:2.3f} ± "
              f"{stddevSwaps_bubbleSort2:2.3f} swaps")
        # print(f"{swapsCollected_bubbleSort2}")
        print(f"ratio: {(meanSwaps_bubbleSort /
                        meanSwaps_bubbleSort2):2.3f}")
        print("-" * 40)


#    # Sort and display once to make verify that the algorithm works
#    randomNumbers = generateRandomList(MIN, MAX, N)
#    # Sort the list and collect statistics
#    (sortedRandomNumbers, _, _) = bubbleSort2(randomNumbers)
#    print(f"in = {randomNumbers}")
#    print(f"out = {sortedRandomNumbers}")

    # Make plots
    fig, (exe, comp, swap) = plt.subplots(nrows=1, ncols=3,
                                        num='performance',
                                        sharey=False
                                        )
    exe.plot(LIST_LENGTHS, exe_bubbleSort)
    exe.plot(LIST_LENGTHS, exe_bubbleSort2)
    exe.set_xlabel('list length')
    exe.set_ylabel('execution time (s)')
    # plt.legend(["bubblesort", "bubblesort+"])
    # exe.set_xticklabels(LIST_LENGTHS)
    # plt.show()


    comp.plot(LIST_LENGTHS, comp_bubbleSort)
    comp.plot(LIST_LENGTHS, comp_bubbleSort2)
    comp.set_xlabel('list length')
    comp.set_ylabel('comparisons')
    # plt.legend(["bubblesort", "bubblesort+"])
    # comp.set_xticklabels(LIST_LENGTHS)
    # plt.show()

    swap.plot(LIST_LENGTHS, swaps_bubbleSort)
    swap.plot(LIST_LENGTHS, swaps_bubbleSort2)
    swap.set_xlabel('list length')
    swap.set_ylabel('swaps')
    plt.legend(["bubblesort", "bubblesort2"])
    # comp.set_xticklabels(LIST_LENGTHS)
    fig.dpi = FIG_DPI
    # fig.set(figwidth=3000 / fig.dpi, figheight=1600 / fig.dpi)
    fig.set(figwidth=FIG_DIM[0], figheight=FIG_DIM[1])
    plt.show()


if __name__ == "__main__":
    main()
