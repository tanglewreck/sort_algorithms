#!/usr/bin/env python

"""
2025-02-19
sortalgorithms.py

Uses bubblesort and a modified version
of that algorithm to sort lists of numbers.

NOTE: run with '-O' to get rid of (excessive) output

"""


import matplotlib.pyplot as plt

from algorithms.performance import do_measurements
from algorithms.defaults import ALGORITHMS
from algorithms.defaults import CATEGORIES
from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTHS
from algorithms.defaults import ITERATIONS
from algorithms.defaults import TIMEIT_ITERATIONS
from algorithms.defaults import TIMEIT_REPEAT
from algorithms.bubblesort import bubblesort
from algorithms.bubblesortplus import bubblesort_plus
# from algorithms.bubblesort import bubblesort_2
# from algorithms.bubblesort import bubblesort_3

def main() -> None:
    """
    Measure execution time, mean number of comparisons
    and mean number of swaps of sort algorithms.
    """

    # main()
    print("Measuring performance...\n"
          f"Number of iterations: {ITERATIONS} \n"
          f"Number of iterations (timeit): {TIMEIT_ITERATIONS}\n"
          f"List lengths: {[int(l) for l in list(LIST_LENGTHS)]}\n")

    # Initialise data-structure
    data = {}
    for algo in ALGORITHMS:
        data[algo] = {'algorithm': algo.__name__}
        for category in CATEGORIES:
            data[algo][category] = {'name': category}
            for list_length in LIST_LENGTHS:
                data[algo][category][list_length] = {'mean': 0.0, 'stddev': 0.0}

    # Collect data, means and stddevs for each category
    for list_length in LIST_LENGTHS:
        for algorithm in ALGORITHMS:
            (data[algorithm]['elapsed'][list_length],
             data[algorithm]['comp'][list_length],
             data[algorithm]['swaps'][list_length]) = do_measurements(algorithm,
                                                         list_length,
                                                         iterations=ITERATIONS,
                                                         timeit_repeat=TIMEIT_REPEAT,
                                                         timeit_iterations=TIMEIT_ITERATIONS)
        print(".")
    print()


    # Print results
    for algo in ALGORITHMS:
        print("=" * 40, sep="")
        print(f"algorithm: {data[algo]['algorithm']}")
        print("=" * 40, sep="")
        for l in LIST_LENGTHS:
            print(f"list length: {l}")
            for category in CATEGORIES:
                print(f"\t{category}: "
                      f"{data[algo][category][l]['mean']:6.4f} "
                      f"± {data[algo][category][l]['stddev']:6.4f}")
            print("-" * 40, sep="")
        print("\n\n")

    # Plot results (means)
    plot_data = {}
    for algorithm in ALGORITHMS:
        plot_data[algorithm] = {}
        for category in CATEGORIES:
            plot_data[algorithm][category] = []
            for l in LIST_LENGTHS:
                plot_data[algorithm][category].append(
                        data[algorithm][category][l]['mean'])

    fig, axs = plt.subplots(nrows=1,
                                             ncols=3,
                                             num="performance",
                                             sharey=False)
    for k, ax in enumerate(axs):
        ax.plot(LIST_LENGTHS,
                 plot_data[bubblesort][CATEGORIES[k]],
                 color='green',
                 label="bubblesort")
        ax.plot(LIST_LENGTHS,
                 plot_data[bubblesort_plus][CATEGORIES[k]],
                 color='orange',
                 label="bubblesort+")

        # ax.set_xticks(LIST_LENGTHS)
        ax.set_xlabel('list length')
        ax.set_ylabel(CATEGORIES[k])
        ax.legend()

    fig.dpi = FIG_DPI
    fig.set(figwidth=FIG_DIM[0], figheight=FIG_DIM[1])
    plt.show()


if __name__ == "__main__":
    main()
