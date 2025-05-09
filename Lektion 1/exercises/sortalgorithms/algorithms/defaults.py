"""
    NAME
        defaults.py
    DESCRIPTION
        Defaults for sort algorithms and performance measurements.
    AUTHOR
        mier
    DATE
        2025-02-19
    VERSION
        2025-05-05
    
"""
import numpy as np
# pylint: disable=unused-import
from . bubblesort import bubblesort
from . bubblesort import bubblesort_nocopy
from . bubblesort import bubblesort2
from . bubblesort import bubblesort2_nocopy
from . bubblesort import bubblesort3
from . bubblesort import bubblesort3_nocopy
from . insertionsort import insertionsort
from . insertionsort import insertionsort2
from . insertionsort import insertionsort3
# pylint: enable=unused-import

__all__ =  ["ALGORITHMS", "ALGOSALL"]
__all__ += ["BS", "BSALL", "IS"]
__all__ += ["COLUMNS"]
__all__ += ["FIG_DIM", "FIG_DPI"]
__all__ += ["ITERATIONS"]
__all__ += ["LENGTH_DEFAULT", "LIST_LENGTHS"]
__all__ += ["LIST_LENGTHS_2"]
__all__ += ["LOWER", "UPPER"]
__all__ += ["SAVEPATH"]
__all__ += ["TIMEIT_ITERATIONS", "TIMEIT_REPEAT"]

# pylint: disable=wildcard-import, unused-wildcard-import, unused-import

# ALGORITHMS
ALGORITHMS = (bubblesort, bubblesort2, bubblesort2_nocopy,
              insertionsort, insertionsort3, insertionsort3)
BS = (bubblesort, bubblesort2)
BSNCP = (bubblesort_nocopy, bubblesort2_nocopy)
BSALL = (bubblesort, bubblesort_nocopy, bubblesort2, bubblesort2_nocopy)
IS = (insertionsort, )
IS2 = (insertionsort2, )
IS3 = (insertionsort3, )
ISALL = IS + IS2 + IS3
ALGOSALL = BS + IS
ALGORITHMS = BS + IS2 + IS3
#
COLUMNS = ('t', 'comps', 'swaps')
LENGTH_DEFAULT = 10
FIG_DIM = (21, 8)
FIG_DPI = 150
# List-lenghts examples:
# LIST_LENGTHS = range(2, 100)
# LIST_LENGTHS = np.arange(2,100)
# LIST_LENGTHS = np.arange(10, 100, 10)
# LIST_LENGTHS = np.append(LIST_LENGTHS, np.arange(100, 301, 50))
# LIST_LENGTHS = np.arange(100, 201, 25)
# LIST_LENGTHS = np.append(np.arange(2,10) + np.arange(10, 100, 10))
# A somewhat complex case...
LIST_LENGTHS_2 = np.append(np.arange(10, 100, 10),
                         np.append(
                             np.append(
                                 np.append(np.arange(100, 200, 50),
                                           np.arange(200, 600, 100)),
                                 np.arange(600, 1200, 200)),
                             np.array([1500, 2000])))
# --> array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
#            150, 200, 300, 400, 500, 600, 800, 1000,
#            1500, 2000])
#
# LIST_LENGTHS = np.array([10, 25, 50, 100, 150, 200, 250, 300])
# LIST_LENGTHS = np.arange(10, 100, 10)
LIST_LENGTHS = np.append(np.arange(10, 110, 10),
                         [150, 200, 250, 300, 350, 400, 450, 500])
# Min/max sizes of a random number
LOWER, UPPER = 1, 10_000
# Number of iterations while measuring performance (comparisons, swaps)
# ITERATIONS = 200
ITERATIONS = 10
# Number of iterations using the timeite module
# TIMEIT_ITERATIONS = 20
# TIMEIT_REPEAT = 20
TIMEIT_ITERATIONS = 10
TIMEIT_REPEAT = 10
# Directory where generated lists are saved:
SAVEPATH = "lists/"
