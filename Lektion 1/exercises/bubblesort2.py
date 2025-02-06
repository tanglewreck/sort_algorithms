# coding: utf-8
import numpy as np
import timeit

L = [int(x) for x in np.random.randint(1,100,7,dtype=int)]

def bubbleSort(theList: list = L):
    l = theList + []
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(l) - 1):
            li = l[index]
            li1 = l[index + 1]
            if li > li1:
                swapped = True   
                print(f"iteration {index + 1}: {l}: {li} > {li1}: swapped")
                l[index], l[index + 1] = l[index + 1], l[index]
            else:
                print(f"iteration {index + 1}: {l}: {li} < {li1}")
        print()
    return l
    

def main():
    bulleSort(L)

if __name__ == "__main__":
    t = timeit.Timer("main")
    elapsed = t.timeit(100_000_000)
    print(elapsed)
