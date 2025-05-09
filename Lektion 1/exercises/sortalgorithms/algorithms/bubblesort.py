# coding: utf-8
"""
    NAME
        bubblesort

    DESCRIPTION
        Various implementations of the bubble sort algorithm.

    DATE
        2025-04-01

    REFERENCES
        Wikipedia: https://en.wikipedia.org/wiki/bubblesort

"""
# pylint: disable=consider-using-enumerate

__all__ = ["bubblesort",
           "bubblesort_nocopy",
           "bubblesort2",
           "bubblesort2_nocopy",
           "bubblesort3",
           "bubblesort3_nocopy"]

# xpylint: disable=import-error
# xpylint: disable=unused-import
# import ipdb
# xpylint: enable=import-error
# xpylint: enable=unused-import
import numpy as np

def bubblesort(arr: np.ndarray, reverse: bool = False) -> tuple:
    """
        Vanilla bubble sort (https://en.wikipedia.org/wiki/bubblesort).

        Parameters
        _________
        arr : array_like
              Array to be sorted.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        arr_copy, ncomps, nswaps 
            arr_copy : array_like, sorted copy of 'arr'
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    arr_copy = arr.copy()
    nswaps = 0
    ncomps = 0
    for _ in range(len(arr_copy)):
        for index in range(len(arr_copy) - 1):
            ncomps += 1
            if arr_copy[index] > arr_copy[index + 1]:
                nswaps += 1
                (arr_copy[index],
                 arr_copy[index + 1]) = (arr_copy[index + 1],
                                          arr_copy[index])
    if reverse:
        return (arr_copy[::-1], ncomps, nswaps)
    return (arr_copy, ncomps, nswaps)


def bubblesort_nocopy(arr: np.ndarray, reverse: bool = False) -> tuple:
    """
        Vanilla bubble sort (https://en.wikipedia.org/wiki/bubblesort).

        Sorts 'arr' inline (no copy of 'arr' made).

        Parameters
        _________
        arr : array_like
              Array to be sorted.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        arr, ncomps, nswaps 
            arr : array_like, 'arr' sorted (inline)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    nswaps = 0
    ncomps = 0
    for _ in range(len(arr)):
        for index in range(len(arr) - 1):
            ncomps += 1
            if arr[index] > arr[index + 1]:
                nswaps += 1
                (arr[index],
                 arr[index + 1]) = (arr[index + 1],
                                          arr[index])
    if reverse:
        return (arr[::-1], ncomps, nswaps)
    return (arr, ncomps, nswaps)


def bubblesort2(arr: np.ndarray, reverse: bool = False) -> tuple:
    """
        Optimised bubble sort (https://en.wikipedia.org/wiki/bubblesort)

        Parameters
        _________
        arr : array_like
              Array to be sorted.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        arr_copy, ncomps, nswaps 
            arr_copy : array_like, sorted copy of 'arr'
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    arr_copy = arr.copy()
    done = False
    ncomps, nswaps = 0, 0
    # Stop when done, i.e. no swaps have been made.
    # This should speed up the algorithm somewhat
    # compared to 'standard' bubble sort.
    while not done:
        done = True
        for index in range(len(arr_copy) - 1):
            ncomps += 1
            if arr_copy[index] > arr_copy[index + 1]:
                done = False
                nswaps += 1
                (arr_copy[index],
                 arr_copy[index + 1]) = (arr_copy[index + 1],
                                          arr_copy[index])
    if reverse:
        return (arr_copy[::-1], ncomps, nswaps)
    return (arr_copy, ncomps, nswaps)


def bubblesort2_nocopy(arr: np.ndarray, reverse: bool = False) -> tuple:
    """
        Optimised bubble sort (https://en.wikipedia.org/wiki/bubblesort).
        Sorts 'arr' inline.

        Parameters
        _________
        arr : array_like
              Array to be sorted.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        arr, ncomps, nswaps 
            arr : array_like, 'arr' sorted (inline)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    done = False
    ncomps, nswaps = 0, 0
    # Stop when done, i.e. no swaps have been made.
    # This should speed up the algorithm somewhat
    # compared to 'standard' bubble sort.
    while not done:
        done = True
        for index in range(len(arr) - 1):
            ncomps += 1
            if arr[index] > arr[index + 1]:
                done = False
                nswaps += 1
                (arr[index],
                 arr[index + 1]) = (arr[index + 1],
                                          arr[index])
    if reverse:
        return (arr[::-1], ncomps, nswaps)
    return (arr, ncomps, nswaps)


def bubblesort3(arr: np.ndarray, reverse: bool = False) -> tuple:
    """
        Optimised bubble sort* (https://en.wikipedia.org/wiki/bubblesort).

        *This implementation is rather more like the insertion sort 
         algorithm (https://en.wikipedia.org/wiki/insertionsort).

        Parameters
        _________
        arr : array_like
              Array to be sorted.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        arr, ncomps, nswaps 
            arr : array_like, 'arr' sorted (inline)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    arr_copy = arr.copy()
    nswaps = 0
    ncomps = 0
    for index_one in range(len(arr_copy)):
        for index_two in range(len(arr_copy) - 1):
            ncomps += 1
            if arr_copy[index_one] < arr_copy[index_two]:
                nswaps += 1
                (arr_copy[index_one],
                 arr_copy[index_two]) = (arr_copy[index_two],
                                          arr_copy[index_one])
    if reverse:
        return (arr_copy[::-1], ncomps, nswaps)
    return (arr_copy, ncomps, nswaps)


def bubblesort3_nocopy(arr: np.ndarray, reverse: bool = False) -> tuple:
    """
        Optimised bubble sort* (https://en.wikipedia.org/wiki/bubblesort).

        Sorts 'arr' inline (no copy of 'arr' is made).

        *This implementation is rather more like the insertion sort 
         algorithm (https://en.wikipedia.org/wiki/insertionsort).

        Parameters
        _________
        arr : array_like
              Array to be sorte.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        arr, ncomps, nswaps 
            arr : array_like, 'arr' sorted (inline)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    nswaps = 0
    ncomps = 0
    for index_one in range(len(arr)):
        for index_two in range(len(arr) - 1):
            ncomps += 1
            if arr[index_one] < arr[index_two]:
                nswaps += 1
                (arr[index_one],
                 arr[index_two]) = (arr[index_two],
                                          arr[index_one])
    if reverse:
        return (arr[::-1], ncomps, nswaps)
    return (arr, ncomps, nswaps)
