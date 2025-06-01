# coding: utf-8
"""2025-04-30"""

import numpy as np
import pandas as pd
from pandas import DataFrame

LIST_LENGTHS = [10, 20]
def measure_elpased(algo, L = LIST_LENGTHS, iterations = 1, n = 5):
    """Create and return 'time measurement' data"""
    dfs = []
    for length in L:
        for _ in range(iterations):
            d = {"algo": np.repeat(algo, n),
                  "L": np.repeat(length, n),
                  "t": np.random.random(n) * 10 + 1}
            dfs.append(DataFrame(d, columns=["algo", "L", "t"]))
    return pd.concat(dfs, ignore_index=True)


df_bs = measure_elpased("bs", n=10)
df_bsplus = measure_elpased("bs+", n=10)
df = pd.concat((df_bs, df_bsplus), ignore_index=True)
print("dataframe:", df, sep="\n")
print()

df_bs_10 = df.loc[(df.algo == "bs") & (df.L == 10)]
df_bsp_10 = df.loc[(df.algo == "bs+") & (df.L == 10)]

print("means:")
print(df_bs_10["t"].mean())
print(df_bsp_10["t"].mean())
