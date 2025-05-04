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
from algorithms.defaults import LIST_LENGTHS
from algorithms.defaults import ITERATIONS
from algorithms.defaults import TIMEIT_ITERATIONS
from algorithms.defaults import TIMEIT_REPEAT

from algorithms.performance import do_measurements
from algorithms.performance import algorithm_perf
from algorithms.performance import algo_perf
from algorithms.performance import time_it_full


def collect_data() -> tuple:
    """
        NAME
            collect_data()
        DESCRIPTION
            Collect data and return a tuple of
            dataframes of raw data (df_t, df_cs )
            and a dataframe of computed averages.
        """
    # Create lists used to contain pd.DataFrame's
    dfs_t = []
    dfs_cs = []
    for algo in ALGORITHMS:
        for length in LIST_LENGTHS:
            # Initialise two data dicts, one for execution
            # time (data_t) and one for comparisons and swaps
            # (data_cs).
            data_t = {'algorithm': np.repeat(algo.__name__,
                                             TIMEIT_REPEAT),
                            'length': np.repeat(length,
                                                TIMEIT_REPEAT)}
            data_cs = {'algorithm': np.repeat(algo.__name__,
                                              ITERATIONS),
                            'length': np.repeat(length,
                                                ITERATIONS)}
            # Measure execution time, using time_it_full() which
            # returns a list of floats of length TIMEIT_REPEAT.
            # Add the returned list to the data dict.
            t = np.array(time_it_full(algorithm=algo,
                                      timeit_repeat=TIMEIT_REPEAT,
                                      timeit_iterations=TIMEIT_ITERATIONS,
                                      list_length=length))
            data_t['t'] = t
            # Measure execution time, using time_it_full() which
            # returns a list of floats of length TIMEIT_REPEAT.
            # Add the returned list to the data dict (column-name:
            # "elapsed").
            comparisons, swaps = algo_perf(algorithm=algo,
                                           list_length=length)
            # Measure execution time, using time_it_full() which
            # returns a list of floats of length TIMEIT_REPEAT.
            # Add the returned list to the data dict (column-name:
            # "elapsed").
            data_cs['comps'] = comparisons
            data_cs['swaps'] = swaps
            # Convert the data-dicts to dataframes and append
            # to the lists of dataframes.
            df_t = DataFrame(data_t,
                              columns=["algorithm", "length", "t"])
            df_cs = DataFrame(data_cs,
                              columns=["algorithm", "length",
                                       "comps", "swaps"])
            dfs_t.append(df_t)
            dfs_cs.append(df_cs)

    # Concatenate the lists of dataframes
    df_t = pd.concat(dfs_t, ignore_index=True)
    df_cs = pd.concat(dfs_cs, ignore_index=True)

    # Create a dataframe of averages
    dfs = []
    for algo in ALGORITHMS:
        # Initialise np.array objects
        t = np.zeros(len(LIST_LENGTHS))
        comps = np.zeros(len(LIST_LENGTHS))
        swaps = np.zeros(len(LIST_LENGTHS))
        # Compute averages from the data columns of
        # the dataframes (df_t, df_cs). Store into
        # np.array objects.
        t = np.array(
                [df_t.loc[
                    (df_t.algorithm==algo.__name__) &
                    (df_t.length==length)].t.mean()
                 for length in LIST_LENGTHS])
        comps = np.array(
                [df_cs.loc[
                    (df_cs.algorithm==algo.__name__) &
                    (df_cs.length==length)].comps.mean()
                 for length in LIST_LENGTHS])
        swaps = np.array(
                [df_cs.loc[
                    (df_cs.algorithm==algo.__name__) &
                    (df_cs.length==length)].swaps.mean()
                 for length in LIST_LENGTHS])
        # Create a dataframe with columns
        #       "algorithm", "length" (list-length), "t" (execution time),
        #       "comps" (number of comparisons), and "swaps (number of swaps),
        #       using the arrays of computed averages (t, comps, swaps).
        #       Then add the dataframe to the list of dataframes.
        data = DataFrame(
                {'algorithm': algo.__name__,
                 'length': LIST_LENGTHS,
                 't': t,
                 'comps': comps,
                 'swaps': swaps}
                 )
        dfs.append(data)
    # Concatenat the list of dataframes
    df = pd.concat(dfs, ignore_index=True)
    return df_t, df_cs, df
