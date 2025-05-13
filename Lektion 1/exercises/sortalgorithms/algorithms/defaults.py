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
from . bubblesort import bubblesort2
from . bubblesort import bubblesort3
from . insertionsort import insertionsort
from . insertionsort import insertionsort2
from . insertionsort import insertionsort3
from . insertionsort import insertionsortwikipedia_for
from . insertionsort import insertionsortwikipedia_while
# pylint: enable=unused-import

__all__ = ["ALGORITHMS", "ALGOSALL"]
__all__ += ["BS", "BSALL", "IS"]
__all__ += ["COLUMNS"]
__all__ += ["FIG_DIM", "FIG_DPI"]
__all__ += ["ITERATIONS"]
__all__ += ["LENGTH_DEFAULT", "LIST_LENGTHS"]
__all__ += ["LIST_LENGTHS_2"]
__all__ += ["LOWER", "UPPER"]
__all__ += ["SAVEPATH"]

# pylint: disable=wildcard-import, unused-wildcard-import, unused-import

# Directory where generated lists are saved:
SAVEPATH = "lists/"
LENGTH_DEFAULT = 10
# Plot size
FIG_DIM = (30, 15)
FIG_DPI = 100
# ALGORITHMS
ALGORITHMS = (bubblesort, bubblesort2, insertionsort,
              insertionsort3, insertionsort3)
BS1 = (bubblesort, )
BS2 = (bubblesort2, )
BS = (bubblesort, bubblesort2)
BSALL = (bubblesort, bubblesort2 )
IS1 = (insertionsort, )
IS2 = (insertionsort2, )
IS3 = (insertionsort3, )
IS = IS1 + IS2 + IS3
ISWFOR = (insertionsortwikipedia_for, )
ISWWHILE = (insertionsortwikipedia_while, )
ISW = ISWFOR + ISWWHILE
ISALL = IS + ISW
ALGOSALL = BS + IS
ALGORITHMS = IS3 + ISW
#
COLUMNS = ('t', 'comps', 'swaps')

# Number of iterations (=number of arrays to sort) during data-collection.
ITERATIONS = 20
# Min/max sizes of a random number
LOWER, UPPER = 1, 10_000

# List-lenghts examples:
# LIST_LENGTHS = np.arange(10, 100, 10)
# LIST_LENGTHS = np.append(LIST_LENGTHS, np.arange(100, 301, 50))
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
LIST_LENGTHS = np.append(np.arange(10, 110, 10),
                         np.array([150, 200, 250, 300, 350, 400, 450, 500, 750,
                                   1000, 1200]))
LIST_LENGTHS = np.array([50, 100, 200, 300, 400, 500, 750])
