"""
defaults.py

DESCRIPTION
Defaults for sort algorithms and performance measurements.

2025-02-19
"""

# pylint: disable=unused-import

import numpy as np
from . bubblesort import bubblesort, bubblesort_2, bubblesort_3
from . bubblesortplus import bubblesort_plus

__all__ = ["ALGORITHMS"]
__all__ += ["CATEGORIES"]
__all__ += ["FIG_DIM", "FIG_DPI"]
__all__ += ["ITERATIONS"]
__all__ += ["TIMEIT_ITERATIONS", "TIMEIT_REPEAT"]
__all__ += ["LIST_LENGTH", "LIST_LENGTHS", "MIN", "MAX"]

# pylint: disable=wildcard-import, unused-wildcard-import, unused-import

ALGORITHMS = [bubblesort, bubblesort_2, bubblesort_plus]
CATEGORIES = ['elapsed', 'comp', 'swaps']

FIG_DIM = (21, 8)
FIG_DPI = 150
# Default number of numbers in a list
LIST_LENGTH = 10

# LIST_LENGTHS = np.array(list(range(2,100)))
# LIST_LENGTHS = np.array(list(range(10, 100, 10)))
# LIST_LENGTHS = np.array(list(range(2, 101, 4)))
# LIST_LENGTHS = np.append(LIST_LENGTHS, np.arange(100, 301, 50))
# LIST_LENGTHS = np.arange(100, 201, 25)
# LIST_LENGTHS = range(10, 110, 10)
# LIST_LENGTHS = np.array(list(range(2,10)) + list(range(10, 100, 10)))
LIST_LENGTHS = np.array(list(range(10, 100, 10)) +
                        list(range(100, 200, 50)) +
                        list(range(200, 600, 100)) +
                        list(range(600, 1200, 200)) +
                        [1500, 2000]
                        )
LIST_LENGTHS = np.array(list(range(10, 100, 10)))
# Min size of a number
MIN = 1
# Max size of a number
MAX = 100
# Number of iterations while measuring performance (comparisons, swaps)
# ITERATIONS = 200
ITERATIONS = 2
# Number of iterations using the timeite module
# TIMEIT_ITERATIONS = 20
# TIMEIT_REPEAT = 20
TIMEIT_ITERATIONS = 10
TIMEIT_REPEAT = 5
