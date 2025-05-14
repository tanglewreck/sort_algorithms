# coding: utf-8
"""
    NAME
        insertionsort

    DESCRIPTION
        Various implementations of the insertion sort algorithm

        The algorithm works by repeatedly iterating through the array,
        comparing the first element of the array with each of the following
        elements, swapping places, switching places if the first is
        larger. This puts the smallest element at the head of the array.

        Because of this, we need only to sort successively short array slices,
        ignoring the already sorted elements.

        Another way of putting this is that the array elements that are moved
        to the head of the array are all in their correct position, so we can
        ignore those elements as we progress further down the array.

    DATE
        2025-05-04

    REFERENCES
        Wikipedia: https://en.wikipedia.org/wiki/insertionsort

"""
__all__ = ["insertionsort",
           "insertionsort2",
           "insertionsort3",
           "insertionsortwikipedia_for",
           "insertionsortwikipedia_while"
           ]

# xpylint: disable=import-error
# xpylint: disable=unused-import
# import ipdb
# xpylint: enable=import-error
# xpylint: enable=unused-import
import numpy as np


def insertionsortwikipedia_for(arr: np.ndarray,
                               copylist: bool = True,
                               reverse: bool = False) -> tuple:
    """
        An implementation of insertion sort
        (https://en.wikipedia.org/wiki/insertionsort).

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
            i ← 1
            while i < length(A)
            x ← A[i]
            j ← i
            while j > 0 and A[j-1] > x
                A[j] ← A[j-1]
                j ← j - 1
            end while
            A[j] ← x
            i ← i + 1
            end while
    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Save array length
    arrlen = len(arr)
    # Count the number of comparisons and swaps
    ncomps, nswaps = 0, 0
    for i in range(1, arrlen):
        # for loops make comparisons
        ncomps += 1
        x = arr[i]
        for j in range(i, -1, -1):
            # for loops make comparisons
            ncomps += 1
            arr[j] = arr[j-1]
            nswaps += 1
            ncomps += 1
            if arr[j-1] < x:
                break
        arr[j] = x
        nswaps += 1
    if reverse:
        arr = np.sort(arr)[::-1]
    return arr, ncomps, nswaps


def insertionsortwikipedia_while(arr: np.ndarray,
                                 copylist: bool = True,
                                 reverse: bool = False) -> tuple:
    """
        An implementation of insertion sort
        (https://en.wikipedia.org/wiki/insertionsort).

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
            i ← 1
            while i < length(A)
            x ← A[i]
            j ← i
            while j > 0 and A[j-1] > x
                A[j] ← A[j-1]
                j ← j - 1
            end while
            A[j] ← x
            i ← i + 1
            end while
    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Save array length
    arrlen = len(arr)
    # Count the number of comparisons and swaps
    ncomps, nswaps = 0, 0
    i = 1
    while i < arrlen:
        # while-loops make comparisons
        ncomps += 1
        x = arr[i]
        j = i
        while j > 0 and arr[j-1] > x:
            # while-loops make comparisons
            ncomps += 2
            arr[j] = arr[j-1]
            nswaps += 1
            j = j - 1
        nswaps += 1
        arr[j] = x
        i += 1
    if reverse:
        arr = np.sort(arr)[::-1]
    return arr, ncomps, nswaps


def insertionsort(arr: np.ndarray,
                  copylist: bool = True,
                  reverse: bool = False) -> tuple:
    """
        An implementation of insertion sort
        (https://en.wikipedia.org/wiki/insertionsort).

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
    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # We count the number of comparisons and swaps made
    ncomps = 0
    nswaps = 0
    # Save length of the array for future reference
    arrlen = len(arr)
    # Count the number of comparisons and swaps made
    # Number of comps is the sum of the arithmetic
    # series 1 + 2 + ... + n = n * (n + 1) /2
    # ncomps = int(arrlen * (arrlen +1) / 2)
    ncomps, nswaps = 0, 0
    # Repeatedly move the smallest element to the top of the array.
    for index_one in range(arrlen):  # outer loop
        # for loops make comparisons
        ncomps += 1
        # If no swaps are made, we're done
        done = True
        for index_two in range(index_one + 1, arrlen):  # inner loop
            # for loops make comparisons
            ncomps += 1
            if arr[index_one] > arr[index_two]:
                # Move the smaller element (arr[index_two])
                # towards the current front of the list
                # (arr[index_one]).
                (arr[index_one],
                 arr[index_two]) = (arr[index_two],
                                    arr[index_one])
                # Update number of comparisons and swaps
                ncomps += 1
                nswaps += 1
                done = False
        if done:
            break
    # Reverse sort
    if reverse:
        return (arr[::-1], ncomps, nswaps)
    # Forward sort
    return (arr, ncomps, nswaps)


def insertionsort2(arr: np.ndarray,
                   copylist: bool = True,
                   reverse: bool = False) -> tuple:
    """
        An optimised implementation of insertion sort
        (https://en.wikipedia.org/wiki/insertionsort).

        Utilises a function for searching for the index of the smallest
        element, in contrast to insertionsort3() which does this
        inline.

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
    """

    def indmin(arr: np.ndarray) -> tuple:
        """Find the index of the smallest element.

            Parameters
            ----------
            'arr' : array_like
                    Array to search.
            Returns
            -------
            index : int
                    Index of the smallest element in 'arr'
            ncomps : int
                     Number of comparisons made during the search.
        """
        index, ncomps = 0, 0
        for k, _ in enumerate(arr):
            ncomps += 1
            if arr[k] < arr[index]:
                index = k
        return index, ncomps

    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Save length of the array for future reference
    arrlen = len(arr)
    # Count the number of comparisons and swaps made
    # Number of comps is the sum of the arithmetic
    # series 1 + 2 + ... + n = n * (n + 1) /2
    # ncomps = int(arrlen * (arrlen +1) / 2)
    ncomps, nswaps = 0, 0
    # Repeatedly move the smallest element to the top of the array.
    for k in range(arrlen):
        # for loops make comparisons
        ncomps += 1
        # Save a slice of the array to search for
        # the (index of) the next smallest element.
        arr_slice_k = arr[k:]
        # Get index of the smallest element in 'the rest' of
        # the list (i.e. the index in the slice arr[k:]).
        ind, nc = indmin(arr_slice_k)
        ind += k
        # Increase the number of comparisons
        ncomps += (nc + 1)
        if arr[k] > arr[ind]:
            # Update # of comparisons and swaps
            ncomps += 1
            nswaps += 1
            # print(f"Swapping index {k} <--> {ind}")
            arr[k], arr[ind] = arr[ind], arr[k]
    # Reverse sort
    if reverse:
        return arr[::-1], ncomps, nswaps
    # Forward sort
    return arr, ncomps, nswaps


def insertionsort3(arr: np.ndarray,
                   copylist: bool = True,
                   reverse: bool = False) -> tuple:
    """
        An optimised implementation of insertion sort
        (https://en.wikipedia.org/wiki/insertionsort).

        Searches for the index of the smallest element is done
        inline instead of using a function (like insertionsort2()) does.

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
    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Save length of the array for future reference
    arrlen = len(arr)
    # Count the number of comparisons and swaps made
    # Number of comps is the sum of the arithmetic
    # series 1 + 2 + ... + n = n * (n + 1) /2
    # ncomps = int(arrlen * (arrlen +1) / 2)
    ncomps, nswaps = 0, 0
    # Repeatedly move the smallest element to the top of the array.
    # The number of swaps
    for k in range(arrlen):
        # for loops make comparisons
        ncomps += 1
        # Save a slice of the array to search for
        # the (index of) the next smallest element.
        arr_slice_k = arr[k:]
        arr_slice_k_len = len(arr_slice_k)
        # Get index of the smallest element in 'the rest' of
        # the list (i.e. the index in the slice arr[k:]).
        ind = 0  # Start at the beginning of the slice
        for i in range(arr_slice_k_len):
            # for loops make comparisons
            ncomps += 1
            if arr_slice_k[i] < arr_slice_k[ind]:
                ind = i
        # Increase the number of comparisons withe number of comparisons
        # made in the loop, i.e. with 'arr_slice_k_len':
        ncomps += arr_slice_k_len
        # Transform the index found in the slice to the index
        # of the same element in the original array.
        ind += k
        if arr[k] > arr[ind]:
            # Increase the number of comparisons and swaps
            ncomps += 1
            nswaps += 1
            # print(f"Swapping index {k} <--> {ind}")
            arr[k], arr[ind] = arr[ind], arr[k]
    # Reverse sort
    if reverse:
        return arr[::-1], ncomps, nswaps
    # Forward sort
    return arr, ncomps, nswaps
