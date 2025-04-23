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

from algorithms.performance import time_it
from algorithms.performance import algorithm_performance
from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTH, LIST_LENGTHS
from algorithms.defaults import MIN, MAX
from algorithms.defaults import ITERATIONS, TIMEIT_ITERATIONS
from algorithms.defaults import MEASUREMENTS
from algorithms.bubblesortplus import bubblesort_plus
from algorithms.bubblesort import bubblesort
from algorithms.bubblesort import bubblesort_2
from algorithms.bubblesort import bubblesort_3
# from algorithms.utils import generateRandomList

# LIST_LENGTHS = np.array([2, 5])
# LIST_LENGTHS = np.append(LIST_LENGTHS, np.arange(10, 100, 10))
print(f"LIST_LENGTHS: {LIST_LENGTHS}")

PERF_DATA = {}

def main() -> None:
    """
    Measure execution time, mean number of comparisons
    and mean number of swaps of bubblesort() and
    bubblesort_plus()

    NOTE: This function is too long and contains too many local variables
          (according to pylint, at least)
    """

    # Helper function
    def measurements(no_measurements = MEASUREMENTS,
                     list_length = LIST_LENGTH):

        for k in range(no_measurements):

            if __debug__:
                print("\n", "= " * 40, sep="")
                print(f"Measurement #{k + 1}")

            # Initialise three lists used for collecting
            # performance data of the algorithms. Later used
            # (see below) for comparing the two algorithms.
            executionTimes = []
            mean_comp = []
            mean_swaps = []

            # Once for each algorithm,
            # measure the performance
            for sort_algorithm in (bubblesort_plus, bubblesort):

                if __debug__:
                    print(
    f"Measuring performance of {sort_algorithm.__name__} "
    f"({TIMEIT_ITERATIONS} iterations):")
                # Measure execution time
                elapsed = time_it(algorithm=sort_algorithm,
                                 list_length=list_length)
                executionTimes.append(elapsed)
                if __debug__:
                    print(f"Elapsed = {elapsed:6.4f} seconds ({TIMEIT_ITERATIONS} iterations)")
                # Measure performance in terms of (mean) number of
                # swaps and (mean) number of comparisons
                (meanNumberOfSwaps,
                 meanNumberOfComparisons) = algorithm_performance(
                                                    iterations=ITERATIONS,
                                                    algorithm=sort_algorithm,
                                                    list_length=list_length)
                if __debug__:
                    print(f"Mean number of swaps: {meanNumberOfSwaps:6.4f}")
                    print(f"Mean number of comparisons: {meanNumberOfComparisons}")
                    print("Done.")
                    print("")

                mean_comp.append(meanNumberOfComparisons)
                mean_swaps.append(meanNumberOfSwaps)


            # Add data to overall statistics
            #time_all_bs_plus.append(
            #    executionTimes[0])
            #time_all_bs.append(
            #    executionTimes[1])
            time_all_bs_plus[k] = executionTimes[0]
            time_all_bs[k] = executionTimes[1]

            comp_all_bs_plus[k] = mean_comp[0]
            comp_all_bs[k] = mean_comp[1]

            swaps_all_bs_plus[k] = mean_swaps[0]
            swaps_all_bs[k] = mean_swaps[1]

            # Ratios
            if __debug__:
                print("= " * 40)
                print("Execution time ratio "
                      f"(bubbleSort / bubblesort_plus): {
                            (time_all_bs_plus[k] / executionTimes[0]):2.2f}")
                # (executionTimes[1] / executionTimes[0]):2.2f}")
                print(f"mean number of comparisons ratio "
                      f"(bubbleSort / bubblesort_plus): {
                            (mean_comp[1] / mean_comp[0]):2.2f}")
                print("mean number of swaps ratio "
                      f"(bubbleSort / bubblesort_plus): {
                            (mean_swaps[1] / mean_swaps[0]):2.2f}")
                print("= " * 40)



    # main()
    print(f"""Measuring performance...
Min: {MIN}
Max: {MAX}
Number of iterations: {ITERATIONS}
Number of iterations (timeit): {TIMEIT_ITERATIONS}
Number of measurements: {MEASUREMENTS}""")
    # 'plot' arrays
    exe_bs = []
    exe_bs_plus = []
    comp_bs = []
    comp_bs_plus = []
    swaps_bs = []
    swaps_bs_plus = []
    # Do measurements
    for list_length in LIST_LENGTHS:
        # Initialise three lists used for collecting
        # performance data of each run. Later used
        # (see below) for comparing the two algorithms.

        time_all_bs = np.zeros(MEASUREMENTS)
        time_all_bs_plus = np.zeros(MEASUREMENTS)

        comp_all_bs = np.zeros(MEASUREMENTS)
        comp_all_bs_plus = np.zeros(MEASUREMENTS)

        swaps_all_bs = np.zeros(MEASUREMENTS)
        swaps_all_bs_plus = np.zeros(MEASUREMENTS)

        # Collect data, filling the above numpy arrays with data
        print("\n", "-" * 40, sep="")
        print("list_length =", list_length, "\n")

        measurements(no_measurements=MEASUREMENTS,
                     list_length=list_length)

        #
        # Compute statistics (mean and standard deviation)
        #
        #   Execution time
        mean_time_bs = np.mean(time_all_bs)
        mean_time_bs_plus = np.mean(time_all_bs_plus)
        stddev_time_bs = np.sqrt(np.var(time_all_bs))
        stddev_time_bs_plus = np.sqrt( np.var(time_all_bs_plus))

        #   Comparisons
        mean_comp_bs = np.mean(comp_all_bs)
        mean_comp_bs_plus = np.mean(comp_all_bs_plus)
        stddec_comp_bs = np.sqrt(np.var(comp_all_bs))
        stddec_comp_bs_plus = np.sqrt(np.var(comp_all_bs_plus))

        #   Swaps
        mean_swaps_bs = np.mean(swaps_all_bs)
        mean_swaps_bs_plus = np.mean(swaps_all_bs_plus)
        stddev_swaps_bs = np.sqrt(np.var(swaps_all_bs))
        stddev_swaps_bs_plus = np.sqrt(np.var(swaps_all_bs_plus))

        # Save mean values to 'plot' arrays
        exe_bs.append(mean_time_bs)
        exe_bs_plus.append(mean_time_bs_plus)
        comp_bs.append(mean_comp_bs)
        comp_bs_plus.append(mean_comp_bs_plus)
        swaps_bs.append(mean_swaps_bs)
        swaps_bs_plus.append(mean_swaps_bs_plus)
        #print("-" * 40, "\n",
        #      f"Performance ({MEASUREMENTS} measurements):\n",
        #      "-" * 40, sep="")

        print(f"bubbleSort: {mean_time_bs:2.3f} ± "
              f"{stddev_time_bs:-2.3f} seconds")
        print(f"bubblesort_plus: {mean_time_bs_plus:2.3f} ± "
              f"{stddev_time_bs_plus:-2.3f} seconds")
        print(f"ratio: {(mean_time_bs /
                         mean_time_bs_plus):2.3f}")

        print(f"\nbubbleSort: {mean_comp_bs:2.3f} ± "
              f"{stddec_comp_bs:2.3f} comparisons")
        print(f"bubblesort_plus: {mean_comp_bs_plus:2.3f} ± "
              f"{stddec_comp_bs_plus:2.3f} comparisons")
        print(f"ratio: {(mean_comp_bs /
                         mean_comp_bs_plus ):2.3f}")

        print(f"\nbubbleSort: {mean_swaps_bs:2.3f} ± "
              f"{stddev_swaps_bs:2.3f} swaps")
        print(f"bubblesort_plus: {mean_swaps_bs_plus:2.3f} ± "
              f"{stddev_swaps_bs_plus:2.3f} swaps")
        # print(f"{swaps_all_bs_plus}")
        print(f"ratio: {(mean_swaps_bs /
                        mean_swaps_bs_plus):2.3f}")
        print("-" * 40)


#    # Sort and display once to make verify that the algorithm works
#    randomNumbers = generateRandomList(MIN, MAX, N)
#    # Sort the list and collect statistics
#    (sortedRandomNumbers, _, _) = bubblesort_plus(randomNumbers)
#    print(f"in = {randomNumbers}")
#    print(f"out = {sortedRandomNumbers}")

    # Make plots
    x = np.linspace(0, 100,100)
    fig, ax = plt.subplots()
    ax.plot(x, x**2)
    ax.plot(x, x**3)
    plt.show()

    fig, (exe, comp, swap) = plt.subplots(nrows=1, ncols=3,
                                        num='performance',
                                        sharey=False
                                        )
    exe.plot(LIST_LENGTHS, exe_bs)
    exe.plot(LIST_LENGTHS, exe_bs_plus)
    print(type(exe_bs))
    # exe.plot(LIST_LENGTHS, 2 * exe_bs)
    exe.set_ylabel('execution time (s)')

    # plt.legend(["bubblesort", "bubblesort+"])
    # exe.set_xticklabels(LIST_LENGTHS)
    # plt.show()


    comp.plot(LIST_LENGTHS, comp_bs)
    comp.plot(LIST_LENGTHS, comp_bs_plus)
    comp.plot(LIST_LENGTHS, LIST_LENGTHS)
    comp.set_xlabel('list length')
    comp.set_ylabel('comparisons')
    # plt.legend(["bubblesort", "bubblesort+"])
    # comp.set_xticklabels(LIST_LENGTHS)
    # plt.show()

    swap.plot(LIST_LENGTHS, swaps_bs)
    swap.plot(LIST_LENGTHS, swaps_bs_plus)
    swap.set_xlabel('list length')
    swap.set_ylabel('swaps')
    plt.legend(["bubblesort", "bubblesort+"])
    # comp.set_xticklabels(LIST_LENGTHS)
    fig.dpi = FIG_DPI
    # fig.set(figwidth=3000 / fig.dpi, figheight=1600 / fig.dpi)
    fig.set(figwidth=FIG_DIM[0], figheight=FIG_DIM[1])
    plt.show()


if __name__ == "__main__":
    main()
