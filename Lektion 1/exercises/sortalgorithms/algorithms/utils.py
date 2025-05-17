"""
2025-02-19
Utilities
"""

# pylint: disable=invalid-name

__all__ = ["debug_msg",
           "err_msg",
           "sys_msg",
           "genlist",
           "generate_random_list",
           "get_command_line_arguments",
           "get_args",
           "read_csv",
           "timestamp"]

import argparse
import inspect
import os
import sys
import textwrap
import time

import numpy as np
import pandas as pd

from .defaults import LOWER, UPPER
from .defaults import ITERATIONS
from .defaults import LIST_LENGTHS
from .defaults import SAVEPATH


def get_args():
    """
        get_args()
            Process commandline arguments and return an argparse...object
    """
    parser = argparse.ArgumentParser(add_help=True,
                                     description="sortperf: Test performance "
                                                 "of sorting algorithms",
                                     prog="sortperf"
    )
    help_dict = {
        'debug': 'Print debug info',
        'low': "Lowest (signed) integers to be drawn from the distribution",
        'high': "One above the largest (signed) integer to be drawn "
                "from the distribution",
        'iterations': "Number of lists to sort", 
        'listlength': "List-lengths to test (provide once per list-length)",
        'algorithm': "Algorithm to test (provide multiple times to test "
                     "multiple algorithms. Possible values: bubblesort, "
                     "bubblesort2, bubblesort3, inssort, inssort2, "
                     "inssort3, qsort, qsort2, qsort_iterative"
    }

    parser.add_argument('-d', '--debug',
                        default=False,
                        action='store_true',
                        help=help_dict['debug'])
    parser.add_argument('--low',
                        default=LOWER,
                        type=int,
                        help=help_dict['low'])
    parser.add_argument('--high',
                        default=UPPER,
                        type=int,
                        help=help_dict['high'])
    parser.add_argument('--iterations', '-i',
                        default=ITERATIONS,
                        type=int,
                        help=help_dict['iterations'])
    parser.add_argument('--listlength', '-l',
                        nargs='+',  # at least one required
                        default=LIST_LENGTHS,
                        type=int,
                        help=help_dict['listlength'])
    parser.add_argument('--algorithm', '-a',
                        nargs='+',  # at least one required
                        default=["inssort3", "qsort"],
                        type=str,
                        help=help_dict['algorithm'])
    args = parser.parse_args()
    # Return arguments as an argparse.Namespace object
    debug_msg(f"{args}")
    return args


def get_command_line_arguments(list_length: int,
                            lower: int = LOWER,
                            upper: int = UPPER
                            ) -> tuple:
    """
    Get commandline arguments using sys.argv (instead of using the
    argparse module).

    First argument: lower (smallest integer to generate)
    Second argument: upper (largest integer to generate)
    Third argument: number of integers to generate (=list-length)

    """
    default_length = 10
    try:
        if len(sys.argv) == 1:
            # No commandline arguments
            (lower, upper,
             list_length) = (LOWER, UPPER, default_length)
        elif len(sys.argv) == 2:
            # One commandline argument
            lower = int(sys.argv[1])
        elif len(sys.argv) == 3:
            # Two commandline arguments
            (lower,
             upper) = [int(arg) for arg in sys.argv[1:]]
        elif len(sys.argv) == 4:
            # Three commandline arguments
            (lower,
             upper,
             list_length) = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        print(f"Got a ValueError: {e}", file=sys.stderr)
        raise SystemExit(1) from e

    # Sanity checks
    if upper < lower:
        print(textwrap.dedent(f"""
              WARNING: Maximum must be larger than lower.
              Switching order.
              Usage: {sys.argv[0]}<min> <max> <N>
        """))
        (lower, upper) = (upper, lower)
    if (upper - lower) < (list_length - 1):
        print(f"Distance between lower ({lower}) and upper ({upper}) "
              f"is less than the numbers of numbers to "
              f"generate (default: {list_length}).")
        raise SystemExit(1)

    if __debug__:
        print(f"min, max, list_length = {lower}, {upper}, {list_length}")

    return (lower, upper, list_length)


def read_csv(path: str = None):
    """
        NAME
            read_csv
        DESCRIPTION
            Read data from a csv-file into a pandasd.DataFrame.
        RETURNS
            df : pandas.DataFrame
    """
    if path is None:
        # A crude way to find a file to read...
        try:
            print("No path given. Trying to find one...")
            path = SAVEPATH + sorted(os.listdir(SAVEPATH))[-1]
            print(f"Using path: {path}")
        except OSError as exception:
            print(repr(exception))
            raise SystemExit(1) from exception
    try:
        # pylint: disable=unspecified-encoding
        df = pd.read_csv(path)
        return df
    except OSError as exception:
        print(repr(exception))
        raise SystemExit(1) from exception
    return None


def timestamp() -> str:
    """Return a timestamp as a string"""
    time_format = "%Y-%m-%dT%H.%M.%S"
    return time.strftime(time_format, time.localtime())


def genlist():
    """
        NAME
            genlist
        DESCRIPTION
            Generate a list of random numbers
        DATE
            2025-05-05
        VERSION
            2025-05-05
    """
    print("Reading data into dataframe")
    df: pd.DataFrame = read_csv()
    try:
        # return np.random.randint(lower, upper, length)
        for row in range(len(df)):
            yield df.iloc[:, row]
    except ValueError as e:
        print(e)
        raise SystemExit(1) from e


def generate_random_list(list_length: int,
                         lower: int = LOWER,
                         upper: int = UPPER
                         ) -> list:
    """
    Generate a list of random integers btw min and max, inclusive.
    """
    try:
        return np.random.randint(lower,
                                 upper,
                                 list_length)
    except ValueError as e:
        print(e)
        raise SystemExit(1) from e


def debug_msg(*args, end="\n"):
    """Utility function. Prints debugging info on stderr"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stderr.write(f"({caller}) {msg}{end}")


def err_msg(*args, end="\n"):
    """Utility function. Prints a(n error) message on stderr"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stderr.write(f"({caller}) {msg}{end}")


def sys_msg(*args, end="\n"):
    """Utility function. Prints a message on stdout"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stdout.write(f"({caller}) {msg}{end}")
