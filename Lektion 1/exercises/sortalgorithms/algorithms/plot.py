"""
    2025-04-23
    plot.py


"""

# pylint: disable=invalid-name
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=unused-import
#
import numpy as np
import matplotlib.pyplot as plt

from algorithms.defaults import FIG_DIM, FIG_DPI
from algorithms.defaults import LIST_LENGTHS
#from algorithms.performance import time_it
#from algorithms.performance import algorithm_performance
#from algorithms.defaults import MIN, MAX
#from algorithms.defaults import ITERATIONS, TIMEIT_ITERATIONS
#from algorithms.defaults import MEASUREMENTS
#from algorithms.bubblesortplus import bubblesort_plus
#from algorithms.bubblesort import bubblesort
#from algorithms.bubblesort import bubblesort_2
#from algorithms.bubblesort import bubblesort_3
# from algorithms.utils import generateRandomList

def plots() -> None:
    """
    Plot performance data:
        - execution time (elapsed)
        - number of comparisons
        - number of swaps
    """

    # 'plot' arrays
    exe_bs = []
    exe_bs_plus = []
    comp_bs = []
    comp_bs_plus = []
    swaps_bs = []
    swaps_bs_plus = []

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
