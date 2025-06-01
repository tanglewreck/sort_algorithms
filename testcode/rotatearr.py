# coding: utf-8
import numpy as np

# Python Program to left rotate the array by d positions
# by rotating one element at a time

# Function to left rotate array by d positions
def rotateArr2(arr: np.ndarray, d:int):
    n = len(arr)
    return arr[1:] + [arr[0], ]


a = [1, 2, 3, 4, 5, 6]
d = 1
a = rotateArr2(a, d)
print(a)
