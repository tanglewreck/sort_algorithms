#!/usr/bin/env python3 -O
"""
    NAME
        generator.py
    USAGE
        from algorithms.generator import pregen
    DESCRIPTION
        Pregenerate lists (or numpy arrays) of
        random numbers and, optionally, save
        to disk.
    DATE
        2025-05-05
    VERSION
        2025-05-05
"""


__all__ = ["pregen", "pregenint"]



from random import randint
import sys
# pylint: disable=import-error
# pylint: disable=unused-import
import ipdb  # iPython interface to pdb
# pylint: enable=import-error
# pylint: enable=unused-import
import numpy as np
from pandas import DataFrame
from algorithms import timestamp
from algorithms import SAVEPATH

def read_csv():
    """
        DESCRIPTION
            Read a csv ifile of numbers into a dataframe.
    """
    return None


# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments
def pregenint(low = 0, high = 100, lsize = 10,
              nlists = 10, dtype = np.int64,
              save = False):
    """
        NAME
            pregen
        DESCRIPTION
            Pregenerate lists of random integers.
        PARAMETERS
            low : np.int64 or int
                Lowest integer to be drawn (inclusive)
            high : np.int64 or int
                Largest integer to be drawn (inclusive)
            nlists : integer type
                Number of lists to be generated
            lsize : int
                Output list size (number of integers in a list)
            dtype : optional, defaults to np.int64
                Desired type of the result.
            save  : bool
                If True, the dataframe is saved using the template
                '<timestamp>-<min>-<max>-<lsize>-<nsize>.csv'
        RETURNS
            out : pandas.DataFrame
                Dataframe of lists.
    """
    # Generate a dataframe using either np.random.randint or random.randint;
    # shouldn't really matter which is used since pd.DataFrame seems to convert
    # int to np.int64 anyway. Remove the elif-clause when sure of this.
    if dtype is np.int64:
        df = DataFrame({ k: np.random.randint(low, high, lsize) for k in range(nlists)})
    elif dtype is int:
        df = DataFrame({ k: [randint(low, high + 1) for i in range(lsize)]
                                for k in range(nlists)})
    else:
        # Failure, shouldn't get here
        return None

    # Save to disk if asked to
    if save:
        outfile = SAVEPATH + timestamp() + f"_{low}-{high}-{lsize}-{nlists}.csv"
        # ipdb.sset_trace()
        try:
            df.to_csv(outfile, header=True, index=False)
            print(f"Saved dataframe to {outfile}")
        except OSError as exception:
            print(repr(exception))
            raise SystemExit(1) from exception
    if __debug__:
        print(df)
    return df


def pregen(*args):
    """
        NAME
            pregen
        DESCRIPTION
            Alias for pregenint.
            Future update is to return floats.
    """
    return pregenint(*args)


if __name__ == "__main__":
    SAVE = False
    try:
        save_arg = sys.argv[1]
        if save_arg in ("1", "true", "True"):
            SAVE = True
    except IndexError:
        print("Save not specified. Setting 'save' to False")
    pregenint(save=SAVE)
