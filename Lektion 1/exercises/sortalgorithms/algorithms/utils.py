"""
2025-02-19
Utilities 
"""

__all__ = ["generateRandomList"]

import sys
import textwrap

import numpy as np
from . defaults import N, MIN, MAX


def generateRandomList(minimum:int = MIN,
                       maximum:int = MAX,
                       numbersToGenerate:int = N) -> list:
    """
    Generate a list of random integers btw min and max, inclusive.
    """
    try:
        return [int(n) for n in np.random.randint(minimum, maximum, numbersToGenerate)]
    except ValueError as e:
        print(e)
        raise SystemExit(1) from e


def getCommandLineArguments(minimum: int = MIN,
                            maximum: int = MAX,
                            numbersToGenerate: int = N) -> tuple:
    """
    Get commandline arguments using sys.argv (instead of using the
    argparse module).

    First argument: minimum (smallest integer to generate)
    Second argument: maximum (largest integer to generate)
    Third argument: number of integers to generate (=list-length)

    """

    try:
        if len(sys.argv) == 1:
            # No commandline arguments
            (minimum,
             maximum,
             numbersToGenerate) = (MIN, MAX, N)
        elif len(sys.argv) == 2:
            # One commandline argument
            minimum = int(sys.argv[1])
        elif len(sys.argv) == 3:
            # Two commandline arguments
            (minimum,
             maximum)  = [int(arg) for arg in sys.argv[1:]]
        elif len(sys.argv) == 4:
            # Three commandline arguments
            (minimum,
             maximum,
             numbersToGenerate)  = [int(arg) for arg in sys.argv[1:]]
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
    if (maximum - minimum ) < (numbersToGenerate - 1):
        print(f"Distance between minimum ({minimum}) and maximum ({maximum}) "
               "is less than the numbers of numbers to "
               f"generate (default: {N}).")
        raise SystemExit(1)

    if __debug__:
        print(f"min, max, numbersToGenerate = {minimum}, {maximum}, {numbersToGenerate}")

    return (minimum, maximum, numbersToGenerate)
