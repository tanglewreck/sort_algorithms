import sys
import numpy as np

# coding: utf-8
def fulsort1(ARR):
    A = ARR.copy()
    begin, end = 0, len(A) - 1
    for k in range(len(A)):
        begin, end = k, len(A[k:]) - 1
        if begin > end:
            break
        print(f"begin={begin}, end={end}")
        lo, hi = A.argmin(), A.argmax()
        print(f"lo={lo}, hi={hi}")
        A[begin], A[lo] = A[lo], A[begin]
        A[end], A[hi] = A[hi], A[end]
        print()
    return A


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 100
    arr = np.random.randint(1, 1000, n)
    print(fulsort(arr))
