# coding: utf-8
import numpy as np

D = np.random.randint(1, 20, 20); DATA2
pivot = len(D) - 2
for k in range(pivot, -1, -1):
    print(k, end=" ")
    if D[k] > D[pivot]:
        # x = D[pivot]
        D.append(D[k])
        print(D)
    print()
