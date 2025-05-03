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

__all__ = ["collect_elapsed",
           "collect_comps_swaps"]

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


def collect_elapsed():
    """
        NAME
            collect_elapsed()
        DESCRIPTION
            Collect execution time (elapsed) data and
            return a dataframe of (raw) data and a dataframe
            of computed averages.
        """
    # Create a list used to contain pd.DataFrame's
    dfs = []
    for algo in ALGORITHMS:
        for length in LIST_LENGTHS:
            # Initialise data dict
            elapsed_data = {'algorithm': np.repeat(algo.__name__,
                                                   TIMEIT_REPEAT),
                            'length': np.repeat(length,
                                                TIMEIT_REPEAT)}
            # Measure execution time, using time_it_full() which
            # returns a list of floats of length TIMEIT_REPEAT.
            # Add the returned list to the data dict (column-name:
            # "elapsed").
            elapsed = np.array(time_it_full(algorithm=algo,
                                   timeit_repeat=TIMEIT_REPEAT,
                                   timeit_iterations=TIMEIT_ITERATIONS,
                                   list_length=length))
            elapsed_data['elapsed'] = elapsed
            # Convert the data-dict to a DataFrame and append
            # to the list of dataframes.
            df = DataFrame(elapsed_data,
                           columns=["algorithm",
                                    "length",
                                    "elapsed"])
            dfs.append(df)

    # Concatenate the list of dataframes into one
    df = pd.concat(dfs, ignore_index=True)

    # Create a dataframe of averages
    dfs = []
    for algo in ALGORITHMS:
        elapsed_means = np.zeros(len(LIST_LENGTHS))
        for k, length in enumerate(LIST_LENGTHS):
            elapsed_means[k] = df.loc[(df.algorithm==algo.__name__) &
                                    (df.length==length)].elapsed.mean()
        elapsed_data = DataFrame(
                {'algorithm': algo.__name__,
                 'length': LIST_LENGTHS,
                 'means': [
                     df.loc[
                         (df.algorithm==algo.__name__) &
                         (df.length==length)].elapsed.mean()
                     for length in LIST_LENGTHS]}
                 )
        dfs.append(elapsed_data)
    df_means = pd.concat(dfs, ignore_index=True)

    return (df, df_means)


def collect_comps_swaps():
    """
        NAME
            collect_elapsed()
        DESCRIPTION
            Collect execution time (elapsed) data and
            return a dataframe of (raw) data and a dataframe
            of computed averages.
        """
    # Create a list used to contain pd.DataFrame's
    dfs = []
    for algo in ALGORITHMS:
        for length in LIST_LENGTHS:
            # Initialise data dict
            elapsed_data = {'algorithm': np.repeat(algo.__name__,
                                                   TIMEIT_REPEAT),
                            'length': np.repeat(length,
                                                TIMEIT_REPEAT)}
            # Measure execution time, using time_it_full() which
            # returns a list of floats of length TIMEIT_REPEAT.
            # Add the returned list to the data dict (column-name:
            # "elapsed").
            elapsed = np.array(time_it_full(algorithm=algo,
                                   timeit_repeat=TIMEIT_REPEAT,
                                   timeit_iterations=TIMEIT_ITERATIONS,
                                   list_length=length))
            elapsed_data['elapsed'] = elapsed
            # Convert the data-dict to a DataFrame and append
            # to the list of dataframes.
            df = DataFrame(elapsed_data,
                           columns=["algorithm",
                                    "length",
                                    "elapsed"])
            dfs.append(df)

    # Concatenate the list of dataframes into one
    df = pd.concat(dfs, ignore_index=True)

    # Create a dataframe of averages
    dfs = []
    for algo in ALGORITHMS:
        elapsed_means = np.zeros(len(LIST_LENGTHS))
        for k, length in enumerate(LIST_LENGTHS):
            elapsed_means[k] = df.loc[(df.algorithm==algo.__name__) &
                                    (df.length==length)].elapsed.mean()
        elapsed_data = DataFrame(
                {'algorithm': algo.__name__,
                 'length': LIST_LENGTHS,
                 'means': [
                     df.loc[
                         (df.algorithm==algo.__name__) &
                         (df.length==length)].elapsed.mean()
                     for length in LIST_LENGTHS]}
                 )
        dfs.append(elapsed_data)
    df_means = pd.concat(dfs, ignore_index=True)

    return (df, df_means)
