# coding: utf-8
"""
    NAME
        insertionsort.py:
    DESCRIPTION
        Sort a list of numbers using insertion sort.
    AUTHOR
        mier
    VERSION
        2025-05-04

"""
__all__ = ["insertionsort",
           "insertionsort2"]

# xpylint: disable=import-error
# xpylint: disable=unused-import
# import ipdb
# xpylint: enable=import-error
# xpylint: enable=unused-import
import numpy as np

def insertionsort(the_list: list, reverse: bool = False) -> tuple:
    """
        NAME
            insertionsort
        DESCRIPTION
            Sorts a list of numbers using insertion sort
        RETURNS
            1. The sorted list (list_copy)
            2. Number of comparisons (ncomps)
            3. Number of swaps (nswaps)
    """

    # We count the number of comparisons and swaps made
    ncomps = 0
    nswaps = 0

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    list_copy = the_list.copy()

    # Repeatedly iterate through the list of numbers, compare the first element
    # with the rest of the elements in turn, switching places if the first is
    # larger than the other element, thus forcing the smallest element of the
    # list to the head.
    #
    # Since, in each iteration, the smallest number is moved to the head of
    # the list in this way, we can optimise by ignoring those numbers we have
    # already moved.
    #
    # Another way of putting this is that the list elements that are moved to
    # the beginning of the list are all in their correct position, so we can
    # ignore those elements as we progress further down the list.

    # Store the length of the list for easy access later
    list_len = len(list_copy)
    # Forward sort
    for index_one in range(list_len):  # outer loop
        # If no swaps are made, we're done
        done = True
        for index_two in range(index_one + 1, list_len):  # inner loop
            ncomps += 1
            if list_copy[index_one] > list_copy[index_two]:
                # Move the smaller element (list_copy[index_two])
                # towards the current front of the list
                # (list_copy[index_one]).
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                          list_copy[index_one])
                nswaps += 1
                done = False
        if done:
            break
    # Reverse sort
    if reverse:
        return (list_copy[::-1], ncomps, nswaps)
    # Forward sort
    return (list_copy, ncomps, nswaps)


def insertionsort2(the_list: np.array,
                      reverse: bool = False) -> tuple:
    """
        NAME
            insertionsort2
        DESCRIPTION
            Insertion sort Improved: Optimised version of
            insertion sort w/ significantly fewer swaps
            (not that that seems to make any difference
            on Windows).
            
            Sorts a list of numbers using insertion sort
        RETURNS
            1. The sorted list (l_c)
            2. Number of comparisons (ncomps)
            3. Number of swaps (nswaps)
    """
    def indmin(l: np.array) -> np.int64:
        """Return index of smallest element"""
        ind = 0
        nc = 0
        for k, _ in enumerate(l):
            nc += 1
            if l[k] < l[ind]:
                ind = k
        return ind

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    l_c = the_list.copy()
    # Save length of list for future reference
    list_len = len(l_c)
    # We count the number of comparisons and swaps made
    # ncomps = np.sum(np.arange(1, list_len + 1))
    ncomps = sum(range(1, list_len + 1))
    nswaps = 0
    # Repeatedly move the smallest element to the top of the array.
    # The number of swaps
    for k in range(list_len):
        # Get index of the smallest element in 'the rest' of
        # the list (i.e. in the list-slice l_c[k:]).
        ind = indmin(l_c[k:]) + k
        # Increase the number of comparisons
        if l_c[k] > l_c[ind]:
            nswaps += 1
            # print(f"Swapping index {k} <--> {ind}")
            l_c[k], l_c[ind] = l_c[ind], l_c[k]
        # print("post: ", l_c)
        # print()
    # ipdb.sset_trace()
    # Reverse sort
    if reverse:
        return l_c[::-1], ncomps, nswaps
    # Forward sort
    return l_c, ncomps, nswaps
