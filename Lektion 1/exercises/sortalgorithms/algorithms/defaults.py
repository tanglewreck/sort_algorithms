"""
2025-02-19
Defaults for sort algorithms and
performance measurements.
"""
__all__ = ["ITERATIONS", "TIMEIT_ITERATIONS"]
__all__ += ["LIST_LENGTH","LIST_LENGTHS", "MIN", "MAX"]
__all__ += ["FIG_DIM", "FIG_DPI"]

import numpy as np

FIG_DIM = (21, 8)
FIG_DPI = 150
# Number of numbers in a list
LIST_LENGTH = 10
### LIST_LENGTHS = np.array(list(range(2,100)))
### LIST_LENGTHS = np.array(list(range(10, 100, 10)))
### LIST_LENGTHS = np.array(list(range(2, 101, 4)))

### LIST_LENGTHS = np.append(LIST_LENGTHS, np.arange(100, 301, 50))

# LIST_LENGTHS = np.arange(100, 201, 25)
LIST_LENGTHS = np.arange(5, 55, 5)
### LIST_LENGTHS = np.array(list(range(2,10)) + list(range(10, 100, 10)))
# Min size of a number
MIN = 1
# Max size of a number
MAX = 100

# Number of iterations while measuring performance
ITERATIONS = 10
# Number of iterations using the timeite module
TIMEIT_ITERATIONS = 100
# Number of measurements (the number of
# times to run each test)
MEASUREMENTS = 10
