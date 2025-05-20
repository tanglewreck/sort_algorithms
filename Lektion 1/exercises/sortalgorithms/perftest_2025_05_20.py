# coding: utf-8
"""perftest 2025-05-20"""

# pylint: disable=unused-import
from collections.abc import Callable
from functools import partial
import timeit
import numpy as np
from algorithms.bubblesort import bubblesort as bs
from algorithms.bubblesort import bubblesort2 as bs2
from algorithms.bubblesort import bubblesort3 as bs3
from algorithms.inssort import inssort as ins
from algorithms.inssort import inssort2 as ins2
from algorithms.inssort import inssort3 as ins3
from algorithms.inssort import inssort_wikipedia_while as insww
from algorithms.inssort import inssort_wikipedia_for as inswf
from algorithms.qsort import qsort as qs
from algorithms.qsort import qsort2 as qs2
from algorithms.qsort import qsort_iterative as qsi
from algorithms.qsort import qsort_iterative2 as qsi2


ALGS2 = [bs, bs2, bs3, ins, ins2, ins3, inswf, insww, qsi2]


# def fw(algo: Callable[[np.ndarray, int, int, bool, bool], tuple],
def fw(algo, l: np.ndarray) -> tuple:
    """wrapper"""
    return algo(l, 0, len(l) -1, True, False)[1:]


def tw(func, arr: np.ndarray, n: int):
    """tw"""
    f = partial(func, arr, 0, len(arr) -1, copylist=True)
    t = timeit.Timer(f)
    return func.__name__, t.timeit(n)


def main():
    """main"""
    n = 100
    # pylint: disable=unused-variable
    ls = np.arange(0, n + 1)
    lr = np.arange(n, -1, -1)
    lrand = np.random.randint(0, 10_000, n)
    for a in ALGS2:
        l = lrand.copy()
        ret = tw(a, l, 1)
        print(": ".join([str(x) for x in ret]))


if __name__ == "__main__":
    main()
