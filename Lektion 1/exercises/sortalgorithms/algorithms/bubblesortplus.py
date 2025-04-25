# coding: utf-8

"""
    bubblesortplus.py:

    Sort a list of numbers in increasing order using
    a modified version of bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of comparisons made
        3. Number of swaps made during the sorting
"""

__all__ = ["bubblesort_plus"]

# pylint: disable=invalid-name


def bubblesort_plus(the_list: list, reverse: bool = False) -> tuple:
    """
    This functions sorts a list of numbers using a modified version
    of bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made

    """
    # Store the length of the list in a variable, for easy access
    list_len: int = len(the_list)

    # We count the number of comparisons and swaps made
    no_comp = 0
    no_swaps = 0

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

    list_len = len(list_copy)
    # Forward sort
    # for index_one in range(0, list_len):  # outer loop
    # for index_one, _ in enumerate(list_copy):  # outer loop
    for index_one in range(list_len):  # outer loop
        # If no swaps are made, we're done
        done = True
        for index_two in range(index_one + 1, list_len):  # inner loop
            no_comp += 1
            if list_copy[index_one] > list_copy[index_two]:
                # Make the swap
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                          list_copy[index_one])
                no_swaps += 1
                done = False
        if done:
            break
    if reverse:
        return (list_copy[::-1], no_comp, no_swaps)
    return (list_copy, no_comp, no_swaps)
