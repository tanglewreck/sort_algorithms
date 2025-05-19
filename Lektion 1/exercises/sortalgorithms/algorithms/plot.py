"""
    plot.py

    DESCRIPTION
    plot data

    2025-04-25
"""

# pylint: disable=import-error, unused-import
# import ipdb
# # pylint: enable=import-error, unused-import

import matplotlib.pyplot as plt
from pandas import DataFrame

from algorithms.defaults import ALGORITHMS
from algorithms.defaults import COLUMNS
from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTHS

__all__ = ["plot_data"]


def plot_data(data: DataFrame,
              columns: tuple = COLUMNS) -> None:
    """
        NAME
            plot_data
        DESCRIPTION
            Plot performance data.
    """
    # Start plotting: Create three subplots, all in one
    # row, for 't' (execution time), 'comps' (comparisons),
    # and 'swaps'.
    ncols = len(columns)
    fig, axs = plt.subplots(nrows=1, ncols=ncols,
                            sharex=True, sharey=False,
                            num="Performance plots")
    # Handle the case of only one column to plot separatly:
    if len(columns) == 1:
        column = columns[0]
        for algo in ALGORITHMS:
            axs.plot(LIST_LENGTHS,
                     data.loc[(data.algorithm == algo.__name__)][column],
                     label=algo.__name__)
        axs.set_xlabel('length')
        if column == "t":
            axs.set_ylabel("t (ms)")
        else:
            axs.set_ylabel(column)
        axs.legend()
    # For more than one column:
    else:
        # colours = ("gray", "green", "black",
        colours = ("#101005", "gray", "#300505", "#101050",
                   "#202080", "darkblue", "black", "lightgray",
                   "blue", "red", "lightgreen") * 2
        markers = ("o", "^", "*", "x", "D", "v", ",") * 2
        styles = ("-", "--", "-.", ":") * 2
        for i, ax in enumerate(axs):
            column = columns[i]
            for j, algo in enumerate(ALGORITHMS):
                fmt = f"{markers[j]}{styles[j]}"
                ax.plot(LIST_LENGTHS,
                        data.loc[(data.algorithm == algo.__name__)][column],
                        fmt, label=algo.__name__, color=colours[j])
            ax.set_title(column)
            ax.set_xlabel('length')
            if column == "t":
                # ax.set_ylabel("t (ms)")
                ax.set_title("t (ms)")
            # else:
            #     ax.set_ylabel(column)
            ax.legend()
    fig.dpi = FIG_DPI
    fig.set(figwidth=FIG_DIM[0], figheight=FIG_DIM[1])
    plt.show()
