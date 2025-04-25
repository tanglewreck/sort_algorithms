"""
    plot.py

    DESCRIPTION
    plot data

    2025-04-25
"""

#
# import numpy as np
import matplotlib.pyplot as plt

from algorithms.defaults import ALGORITHMS
from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTHS

__all__ = ["do_plots"]


def do_plots(data: dict, categories: list) -> None:
    """
    Plot performance data:
        - execution time (elapsed)
        - number of comparisons
        - number of swaps
    """

    # Create an array (list) of means, one for
    # each algorithm.
    plot_data = {}
    for algorithm in ALGORITHMS:
        plot_data[algorithm] = {}
        for category in categories:
            plot_data[algorithm][category] = []
            for list_length in LIST_LENGTHS:
                plot_data[algorithm][category].append(
                        data[algorithm][category][list_length]['mean'])

    # Plot results (means)
    fig, axs = plt.subplots(nrows=1, ncols=3,
                            num="performance", sharey=False)
    for k, ax in enumerate(axs):
        for algo in ALGORITHMS:
            ax.plot(LIST_LENGTHS,
                    plot_data[algo][categories[k]],
                    label=algo.__name__)
        ax.set_xlabel('list length')
        ax.set_ylabel(categories[k])
        ax.legend()

    fig.dpi = FIG_DPI
    fig.set(figwidth=FIG_DIM[0], figheight=FIG_DIM[1])
    plt.show()
