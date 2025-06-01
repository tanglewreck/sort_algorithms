"""
    NAME
        algorithms/__init__.py
    DESCRIPTION
        Stuff exported at the package level
    DATE
        2025-05-05
    VERSION
        2025-05-05
"""
# These are used in ../sortperf.py
from .collect import collect_data
from .defaults import ALGORITHMS, ALGOSALL, BS, BSALL, IS
from .defaults import COLUMNS
from .defaults import LENGTH_DEFAULT
from .defaults import ITERATIONS
from .defaults import LIST_LENGTHS
from .defaults import SAVEPATH
from .defaults import LOWER, UPPER
from .plot import plot_data

# These are not necessarily used by
# anything 'above' this package
# (but they are used by modules within
# this package, at least some are).
from .utils import debug_msg
from .utils import err_msg
from .utils import sys_msg
from .utils import timestamp
from .utils import read_csv
from .utils import get_args
# from .utils import generate_random_list
# This one might be used in sortperf.py
# at a later point:
from .utils import get_command_line_arguments

# Export these:
__all__ = [
          # collect.py
          "collect_data",
          # plot.py
          "plot_data",
          # utils.py
          "debug_msg", "err_msg", "sys_msg",
          "get_args",
          "read_csv", "timestamp",
          "get_command_line_arguments",
          # defaults.py
          "ALGORITHMS", "ALGOSALL",
          "BS", "BSALL", "IS",
          "COLUMNS", "ITERATIONS",
          "LENGTH_DEFAULT", "LIST_LENGTHS",
          "SAVEPATH", "LOWER", "UPPER"]


# The imports below are currently not used outside
# this package. They're just there...
#
# from .defaults import FIG_DIM
# from .defaults import FIG_DPI
# from .defaults import UPPER, LOWER
# from .defaults import TIMEIT_ITERATIONS
# from .defaults import TIMEIT_REPEAT

# from .bubblesort import bubblesort
# from .bubblesort import bubblesort_2
# from .bubblesort import bubblesort_3

# from .inssort import inssort
# from .inssort import inssort2
# from .inssort import inssort3

# from .performance import algo_perf
# from .performance import time_it_repeat
