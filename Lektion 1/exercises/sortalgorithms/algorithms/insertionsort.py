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
           "insertionsort3"]

# xpylint: disable=import-error
# xpylint: disable=unused-import
# import ipdb
# xpylint: enable=import-error
# xpylint: enable=unused-import
import numpy as np


def insertionsort(arr: np.ndarray, reverse: bool = False) -> tuple:
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
        arr_copy, ncomps, nswaps
            arr_copy : array_like, sorted copy of 'arr'
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    # We count the number of comparisons and swaps made
    ncomps = 0
    nswaps = 0

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    arr_copy = arr.copy()
    # Save length of the array for future reference
    arrlen = len(arr_copy)
    # Count the number of comparisons and swaps made
    # Number of comps is the sum of the arithmetic
    # series 1 + 2 + ... + n = n * (n + 1) /2
    # ncomps = int(arrlen * (arrlen +1) / 2)
    ncomps = 0
    nswaps = 0

    # Repeatedly move the smallest element to the top of the array.
    for index_one in range(arrlen):  # outer loop
        # If no swaps are made, we're done
        done = True
        for index_two in range(index_one + 1, arrlen):  # inner loop
            ncomps += 1
            if arr_copy[index_one] > arr_copy[index_two]:
                # Move the smaller element (arr_copy[index_two])
                # towards the current front of the list
                # (arr_copy[index_one]).
                (arr_copy[index_one],
                 arr_copy[index_two]) = (arr_copy[index_two],
                                         arr_copy[index_one])
                nswaps += 1
                done = False
        if done:
            break
    # Reverse sort
    if reverse:
        return (arr_copy[::-1], ncomps, nswaps)
    # Forward sort
    return (arr_copy, ncomps, nswaps)


def insertionsort2(arr: np.ndarray, reverse: bool = False) -> tuple:
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
        arr_copy, ncomps, nswaps
            arr_copy : array_like, sorted copy of 'arr'
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

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    arr_copy = arr.copy()
    # Save length of the array for future reference
    arrlen = len(arr)
    # Count the number of comparisons and swaps made
    # Number of comps is the sum of the arithmetic
    # series 1 + 2 + ... + n = n * (n + 1) /2
    # ncomps = int(arrlen * (arrlen +1) / 2)
    ncomps = 0
    nswaps = 0
    # Repeatedly move the smallest element to the top of the array.
    for k in range(arrlen):
        # Save a slice of the array to search for
        # the (index of) the next smallest element.
        arr_slice_k = arr_copy[k:]
        # Get index of the smallest element in 'the rest' of
        # the list (i.e. the index in the slice arr_copy[k:]).
        ind, nc = indmin(arr_slice_k)
        ind += k
        # Increase the number of comparisons
        ncomps += (nc + 1)
        if arr_copy[k] > arr_copy[ind]:
            nswaps += 1
            # print(f"Swapping index {k} <--> {ind}")
            arr_copy[k], arr_copy[ind] = arr_copy[ind], arr_copy[k]
    # Reverse sort
    if reverse:
        return arr_copy[::-1], ncomps, nswaps
    # Forward sort
    return arr_copy, ncomps, nswaps


def insertionsort3(arr: np.ndarray, reverse: bool = False) -> tuple:
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
        arr_copy, ncomps, nswaps
            arr_copy : array_like, sorted copy of 'arr'
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.
    """
    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    arr_copy = arr.copy()
    # Save length of the array for future reference
    arrlen = len(arr_copy)
    # Count the number of comparisons and swaps made
    # Number of comps is the sum of the arithmetic
    # series 1 + 2 + ... + n = n * (n + 1) /2
    # ncomps = int(arrlen * (arrlen +1) / 2)
    ncomps = 0
    nswaps = 0
    # Repeatedly move the smallest element to the top of the array.
    # The number of swaps
    for k in range(arrlen):
        # Save a slice of the array to search for
        # the (index of) the next smallest element.
        arr_slice_k = arr_copy[k:]
        arr_slice_k_len = len(arr_slice_k)
        # Get index of the smallest element in 'the rest' of
        # the list (i.e. the index in the slice arr_copy[k:]).
        ind = 0  # Start at the beginning of the slice
        for i in range(arr_slice_k_len):
            if arr_slice_k[i] < arr_slice_k[ind]:
                ind = i
        # Increase the number of comparisons withe number of comparisons
        # made in the loop, i.e. with 'arr_slice_k_len':
        ncomps += arr_slice_k_len
        # Transform the index found in the slice to the index
        # of the same element in the original array.
        ind += k
        if arr_copy[k] > arr_copy[ind]:
            nswaps += 1
            # print(f"Swapping index {k} <--> {ind}")
            arr_copy[k], arr_copy[ind] = arr_copy[ind], arr_copy[k]
        # Increase the number of comparisons
        ncomps += 1
    # Reverse sort
    if reverse:
        return arr_copy[::-1], ncomps, nswaps
    # Forward sort
    return arr_copy, ncomps, nswaps


# def insertionsort3_nocopy(arr: np.ndarray, reverse: bool = False) -> tuple:
#     """
#         An optimised implementation of insertion sort
#         (https://en.wikipedia.org/wiki/insertionsort).
#
#         Sorts 'arr' inline (no copy of 'arr' made).
#
#         Also does the searches for the index of the smallest
#         element inline instead of using a function (like
#         insertionsort2() does
#
#         Parameters
#         _________
#         arr : array_like
#               Array to be sorted.
#         reverse : bool, optional
#                   Defaults to False, in which case the array is
#                   sorted in ascending order.
#
#         Returns
#         -------
#         arr, ncomps, nswaps
#             arr : array_like, 'arr' sorted (inline)
#             ncomps : int, number of comparisons made by the sorting algorithm
#             nswaps : int, number of swaps made by the sorting algorithm
#     """
#     # Save length of list for future reference
#     arrlen = len(arr)
#     # Count the number of comparisons and swaps made
#     # Number of comps is the sum of the arithmetic
#     # series 1 + 2 + ... + n = n * (n + 1) /2
#     # ncomps = int(arrlen * (arrlen +1) / 2)
#     ncomps = 0
#     nswaps = 0
#     # Repeatedly move the smallest element to the top of the array.
#     # The number of swaps
#     for k in range(arrlen):
#         # Get index of the smallest element in 'the rest' of
#         # the list (i.e. in the list-slice arr[k:]).
#         ind = 0
#         # for i, _ in enumerate(arr[k:]):
#         arr_k_len = len(arr[k:])
#         lc_k = lc[k:]  # make a copy of lc
#         for i in range(lc_k_len):
#             ncomps += 1
#             if lc_k[i] < lc_k[ind]:
#                 ind = i
#         ind += k
#         # Increase the number of comparisons
#         ncomps += 1
#         if lc[k] > lc[ind]:
#             nswaps += 1
#             # print(f"Swapping index {k} <--> {ind}")
#             lc[k], lc[ind] = lc[ind], lc[k]
#         # print("post: ", lc)
#         # print()
#     # ipdb.sset_trace()
#     # Reverse sort
#     if reverse:
#         return lc[::-1], ncomps, nswaps
#     # Forward sort
#     return lc, ncomps, nswaps
