"""
2025-02-19
Utilities
"""

# pylint: disable=invalid-name

__all__ = ["generate_random_list",
           "get_command_line_arguments",
           "debug_msg",
           "err_msg",
           "sys_msg",
           "timestamp"]

import inspect
import sys
import textwrap
import time

import numpy as np
from . defaults import MIN, MAX


def timestamp() -> str:
    """Return a timestamp as a string"""
    time_format = "%Y-%m-%dT%H.%M.%S"
    return time.strftime(time_format, time.localtime())


def generate_random_list(list_length: int,
                         minimum: int = MIN,
                         maximum: int = MAX
                         ) -> list:
    """
    Generate a list of random integers btw min and max, inclusive.
    """
    try:
        return np.random.randint(minimum,
                                 maximum,
                                 list_length)
    except ValueError as e:
        print(e)
        raise SystemExit(1) from e


def get_command_line_arguments(list_length: int,
                            minimum: int = MIN,
                            maximum: int = MAX
                            ) -> tuple:
    """
    Get commandline arguments using sys.argv (instead of using the
    argparse module).

    First argument: minimum (smallest integer to generate)
    Second argument: maximum (largest integer to generate)
    Third argument: number of integers to generate (=list-length)

    """
    default_length = 10
    try:
        if len(sys.argv) == 1:
            # No commandline arguments
            (minimum,
             maximum,
             list_length) = (MIN, MAX, default_length)
        elif len(sys.argv) == 2:
            # One commandline argument
            minimum = int(sys.argv[1])
        elif len(sys.argv) == 3:
            # Two commandline arguments
            (minimum,
             maximum) = [int(arg) for arg in sys.argv[1:]]
        elif len(sys.argv) == 4:
            # Three commandline arguments
            (minimum,
             maximum,
             list_length) = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        print(f"Got a ValueError: {e}", file=sys.stderr)
        raise SystemExit(1) from e

    # Sanity checks
    if maximum < minimum:
        print(textwrap.dedent(f"""
              WARNING: Maximum must be larger than minimum.
              Switching order.
              Usage: {sys.argv[0]}<min> <max> <N>
        """))
        (minimum, maximum) = (maximum, minimum)
    if (maximum - minimum) < (list_length - 1):
        print(f"Distance between minimum ({minimum}) and maximum ({maximum}) "
              f"is less than the numbers of numbers to "
              f"generate (default: {list_length}).")
        raise SystemExit(1)

    if __debug__:
        print(f"min, max, list_length = {minimum}, {maximum}, {list_length}")

    return (minimum, maximum, list_length)


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
