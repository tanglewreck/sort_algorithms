# coding: utf-8
"""
    NAME
        measure
    DESCRIPTION
        Measure performance
    AUTHOR
        mier
    DATE
        2025-05-07
"""
__all__ = ["genarr", "measure", "measurements"]

## xpylint: disable=unused-import
from collections.abc import Callable
from functools import partial
import timeit
import numpy as np
import pandas as pd
# pylint: disable=unused-import
from algorithms.utils import debug_msg, err_msg, sys
from algorithms.defaults import ALGORITHMS, ALGOSALL
from algorithms.defaults import bubblesort, bubblesort_nocopy
from algorithms.defaults import bubblesort2, bubblesort2_nocopy
from algorithms.defaults import insertionsort, insertionsort2, insertionsort3
# pylint: enable=unused-import
from algorithms.defaults import LENGTH_DEFAULT
from algorithms.defaults import LIST_LENGTHS
from algorithms.defaults import LOWER, UPPER
from algorithms.defaults import ITERATIONS



def genarr(low: int = LOWER, high: int = UPPER,
           size = (ITERATIONS, LENGTH_DEFAULT),
           dtype = int):
#            nlists: int = ITERATIONS, llength: int = LENGTH_DEFAULT):
    """
        NAME
            genarr
        DESCRIPTION
            Basically a wrapper around np.random.randint with
            default values provided.
    """
    return np.random.randint(low, high, size, dtype)


def measure(ldata: np.array, algo: Callable = bubblesort,
            nlists: int = ITERATIONS, llength: int = 10,
            verbose = False):
    """Do the measurements"""
    t, comps, swaps = [], [], []
    try:
        # Get number of ldata to sort (nlists)
        # and length of each list (llength) from
        # the shape (2 x 2 tuple) of the ldata
        # variable (np.array):
        # nlists, llength = ldata.shape
        # nlists, llength = ITERATIONS
        if verbose:
            print(f"algorithm {algo.__name__}")
            print(f"ldata.shape {ldata.shape}")
            print(f"llength {llength}")
            print(f"nlists {nlists}")
        if llength > ldata.shape[1]:
            errormsg = f"llength > (list length in ldata ({ldata.shape[1]}))"
            raise IndexError(errormsg)
        for k in range(nlists):
            l = ldata[k][:llength]
            if verbose:
                print(l)
            # Measure number of comparisons and swaps
            _, c, s = algo(l)
            comps.append(c)
            swaps.append(s)
            # Measure execution time
            f = partial(algo, l)
            timer = timeit.Timer(f)
            t.append(timer.timeit(1))
        if verbose:
            print(f"t = {t}")
            print(f"comps = {comps}")
            print(f"swaps = {swaps}")
            print()
            print(f"t.mean = {np.mean(t):01.2f} ± {np.std(t):01.2f}")
            print(f"comps.mean = {np.mean(comps):01.2f} ± {np.std(comps):01.2f}")
            print(f"swaps.mean = {np.mean(swaps):01.2f} ± {np.std(swaps):01.2f}")
    except AttributeError as exception:
        err_msg("Got an AttributeError:")
        err_msg(f"{repr(exception)}")
        raise
    except IndexError as exception:
        err_msg("Got an IndexError:")
        err_msg(f"{repr(exception)}")
        raise
    # return np.mean(t), np.mean(comps), np.mean(swaps)
    # return np.array(t), np.array(comps), np.array(swaps)
    return pd.DataFrame([t, comps, swaps],
                        index=["t", "comps", "swaps"])


def measurements(ldata: list = None, algo: Callable = bubblesort,
             llengths=LIST_LENGTHS, nlists=(ITERATIONS,),
                 verbose = False) -> None:
    """
        Measure performance of a sort algorithm. 
        Wrapper around measure().

        Parameters
        ----------
        ldata : list or numpy array. If None, a (rather large) two-dimensional 
                array is generated using genarr(). 
        algo : Callable – the sort algorithm (a function, not a function *name*).
               Defaults to bubblesort().
        llengths : iterable – a list of listlengths to be tested. Defaults
               to LIST_LENGTHS, imported from algorithms.default.
        nlists : list – the number of lists to be tested. Defaults to 
                 ITERATIONS, imported from algorithms.defaults.

    """
    if max(nlists) > len(ldata):
        errormsg = f"max(nlists) ({max(nlists)}) is too large " \
                   f"(ldata contains only {len(ldata)} lists)"
        raise IndexError(errormsg)
    try:
        print(f"Measuring performance of {algo.__name__}")
        if ldata is None:
            ldata = genarr()
            llengths = [LENGTH_DEFAULT, ]
        for ll in llengths:
            print(f"Current list-length: {ll}",)
            for nl in nlists:
                df = measure(ldata, algo, nlists=nl, llength=ll, verbose=verbose)
                print(f"    nlists (iterations): {nl} :", end="")
                print(f'{"t"}: {df.loc["t"].mean() / 1e-3:2.4f} ± '
                      f'{df.loc["t"].std() / 1e-3:2.4f} ms', end=" ")
                for ind in df.index[1:]:
                    print(f'{ind}: {df.loc[ind].mean():2.2f} ± {df.loc[ind].std():2.2f}', end=" ")
                print()
    except AttributeError as exception:
        err_msg("Got an AttributeError:")
        err_msg(f"{repr(exception)}")
        return None
    except IndexError as exception:
        err_msg("Got an IndexError:")
        err_msg(f"{repr(exception)}")
    return None
