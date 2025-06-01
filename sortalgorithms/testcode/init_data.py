# coding: utf-8
from algorithms.bubblesort import bubblesort
from algorithms.bubblesortplus import bubblesort_plus
from algorithms.defaults import ALGORITHMS, LIST_LENGTHS

def init_data():
    D = {}
    for algo in ALGORITHMS:
        D[algo] = {'name': algo.__name__}
        D[algo]['elapsed'] = {}
        D[algo]['comp'] = {}
        D[algo]['swaps'] = {}
        for l in LIST_LENGTHS:
            D[algo]['elapsed'][l] = {'mean': 0.0, 'stddev': 0.0}
            D[algo]['comp'][l] = {'mean': 0.0, 'stddev': 0.0}
            D[algo]['swaps'][l] = {'mean': 0.0, 'stddev': 0.0}
    return D
