# coding: utf-8
"""
    NAME
        quicksort

    DESCRIPTION

    DATE
        2025-05-12

    REFERENCES
        Wikipedia: https://en.wikipedia.org/wiki/Quicksort

"""
__all__ = ["quicksort"]

# xpylint: disable=import-error
# xpylint: disable=unused-import
# import ipdb
# xpylint: enable=import-error
# xpylint: enable=unused-import
import numpy as np


def quicksort(arr: np.ndarray,
              copylist: bool = True,
              reverse: bool = False) -> tuple:
    """
        An implementation of Quicksort

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
            arr : array_like, sorted copy of 'arr'
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.

        Pseudocode
        ----------
        // Sorts (a portion of) an array, divides it into partitions, then sorts those
        algorithm quicksort(A, lo, hi) is
        if lo >= 0 && hi >= 0 && lo < hi then
            p := partition(A, lo, hi)
            quicksort(A, lo, p) // Note: the pivot is now included
            quicksort(A, p + 1, hi)

        // Divides array into two partitions
        algorithm partition(A, lo, hi) is
            // Pivot value
            pivot := A[lo] // Choose the first element as the pivot

            // Left index
            i := lo - 1

            // Right index
            j := hi + 1

            loop forever
                // Move the left index to the right at least once and while the element at
                // the left index is less than the pivot
                do i := i + 1 while A[i] < pivot

                // Move the right index to the left at least once and while the element at
                // the right index is greater than the pivot
                do j := j - 1 while A[j] > pivot

                // If the indices crossed, return
                if i >= j then return j

                // Swap the elements at the left and right indices
                swap A[i] with A[j]

    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Save array length
    arrlen = len(arr)
    # Count the number of comparisons and swaps
    ncomps, nswaps = 0, 0

    # Code goes here


    if reverse:
        arr = np.sort(arr)[::-1]
    return arr, ncomps, nswaps
