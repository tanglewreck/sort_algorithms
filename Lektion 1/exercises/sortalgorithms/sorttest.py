# coding: utf-8

# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=unused-import
# pylint: disable=disallowed-name
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments
# pylint: disable=too-many-positional-arguments

import functools
import timeit
import numpy as np
from algorithms.bubblesort import bubblesort
from algorithms.bubblesortplus import bubblesort_plus

MIN = 0
MAX = 100

R = 10
I = 100
L = 200
N = 10


def sorttest(algo=bubblesort_plus, n = N,
             lower = MIN, upper = MAX,
             iterations = I, repeat = R,
             length = L, dtype = int,
             verbose = False):

    means2 = []
    means3 = []
    means4 = []

    if dtype == int:
        l3 = np.array(range(lower, upper))
        l4 = np.array(range(lower, upper))[::-1]
    else:
        l3 = np.array(range(lower, upper), dtype=float)
        l4 = np.array(range(lower, upper), dtype=float)[::-1]

    f3 = functools.partial(algo, l3)
    f4 = functools.partial(algo, l4)

    t3 = timeit.Timer(f3)
    t4 = timeit.Timer(f4)

    for _ in range(n):
        if dtype == int:
            l2 = list(np.random.randint(lower, upper, length))
        else:
            l2 = list(np.random.random_sample(length) * (upper - lower) + lower)

        f2 = functools.partial(algo, l2)
        t2 = timeit.Timer(f2)

        lt2 = t2.repeat(repeat, iterations)
        lt3 = t3.repeat(repeat, iterations)
        lt4 = t4.repeat(repeat, iterations)

        means2.append(np.mean(lt2))
        means3.append(np.mean(lt3))
        means4.append(np.mean(lt4))

        # print(f"lt2: {(np.mean(lt2), np.sqrt(np.var(lt2)))}")
        # print(f"lt3: {(np.mean(lt3), np.sqrt(np.var(lt3)))}")
        # print(f"lt4: {(np.mean(lt4), np.sqrt(np.var(lt4)))}")
        # print()

    if verbose:
        print(f"algorithm: {algo.__name__}")
        print()
        print(f"dtype: {dtype}")
        print(f"n: {n}")
        print(f"repeat: {repeat}")
        print(f"timeit iterations: {iterations}")
        print(f"listlenght: {length}")
        print()

        print(f"random list: {np.mean(means2):8.6f} ± {np.sqrt(np.var(means2)):8.6f}")
        print(f"sorted list: {np.mean(means3):8.6f} ± {np.sqrt(np.var(means3)):8.6f}")
        print(f"reversed list:{np.mean(means4):8.6f} ± {np.sqrt(np.var(means4)):8.6f}")
        print()

    return np.mean(means2), np.mean(means3), np.mean(means4)


if __name__ == "__main__":
    sorttest()
