"""
    NAME
        collect.py
    DESCRIPTION
        Collect data of sort algorithms
    DATE
        2025-05-03
"""

# pylint: disable=consider-using-dict-items
# pylint: disable=unused-import

__all__ = ["collect_data"]

# pylint: disable=import-error
import ipdb
# pylint: enable=import-error
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from algorithms.defaults import ALGORITHMS
from algorithms.defaults import ITERATIONS
from algorithms.defaults import LENGTH_DEFAULT
from algorithms.defaults import LIST_LENGTHS
from algorithms.defaults import LOWER, UPPER
from algorithms.performance import measure
from algorithms.performance import genlists


def collect_data() -> tuple:
    """
       Collect data and return a tuple of dataframes one of raw data (df_t, df_cs )

       Parameters
       ----------
       None – everything needed is imported from the algorithms package.

       Returns
       -------
       Two dataframes are returned, as a tuple, one for raw data (df)
       and one for computed averages (df_means)

       Author
       ------
       mier

       Date
       ----
       2025-05-07 (updated)
        """
    # Generate test data (make it LARGE so there's
    # room to spare!)
    lists = genlists(size=(10_000, 10_000))  # 10 000 lists of length 10 000
    #
    # Initialise a list which will contain the generated dataframes
    # (one for each list-length in LIST_LENGTHS).
    dfs = []
    # Do the measurements
    for algo in ALGORITHMS:
        for length in LIST_LENGTHS:
            data = measure(lists, algo=algo, nlists=ITERATIONS, llength=length)
            dfs.append(data)
    df = pd.concat(dfs, ignore_index=True)

    # Create a dataframe of averages
    dfs = []
    for algo in ALGORITHMS:
        # Initialise np.array objects
        t = np.zeros(len(LIST_LENGTHS))
        comps = np.zeros(len(LIST_LENGTHS))
        swaps = np.zeros(len(LIST_LENGTHS))
        # Compute averages; store in arrays
        t = np.array([df.loc[
                     (df.algorithm==algo.__name__) &
                     (df.length==length)].t.mean()
                 for length in LIST_LENGTHS])
        comps = np.array([df.loc[
                         (df.algorithm==algo.__name__) &
                         (df.length==length)].comps.mean()
                 for length in LIST_LENGTHS])
        swaps = np.array([df.loc[
                         (df.algorithm==algo.__name__) &
                         (df.length==length)].swaps.mean()
                 for length in LIST_LENGTHS])
        # Create a dataframe with columns
        #       "algorithm", "length" (list-length), "t" (execution time),
        #       "comps" (number of comparisons), and "swaps (number of swaps),
        #       using the arrays of computed averages (t, comps, swaps).
        #       Then add the dataframe to the list of dataframes.
        df_means = DataFrame({'algorithm': algo.__name__,
                              'length': LIST_LENGTHS,
                              't': t,
                              'comps': comps,
                              'swaps': swaps})
        dfs.append(df_means)
    # Concatenate into one dataframe
    df_means = pd.concat(dfs, ignore_index=True)

    # Return two dataframes, one for raw data and
    # one for averages
    return df, df_means
