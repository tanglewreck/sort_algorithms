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
__all__ = ["insertionsort"]


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
            # Find the position of the smalles element of
            # list_copy[index_one:], then move that element to
            # the front of the list
            # At first, assume that the first element is the largest
            index_min = index_one
            ncomps += 1
            if list_copy[index_one] > list_copy[index_two]:
                index_min = index_two
                # Move the smaller element towards the front of
                # the list
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                          list_copy[index_one])
                nswaps += 1
                done = False
            if __debug__:
                print(f"Smallest at position {index_min} ({the_list[index_min]})")
        if done:
            break
    # Reverse sort
    if reverse:
        return (list_copy[::-1], ncomps, nswaps)
    # Forward sort
    return (list_copy, ncomps, nswaps)
