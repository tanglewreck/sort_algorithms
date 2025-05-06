# coding: utf-8
"""
    bubblesort.py

    Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
# pylint: disable=consider-using-enumerate

__all__ = ["bubblesort",
           "bubblesort_2",
           "bubblesort_2_2",
           "bubblesort_3"]


def bubblesort_2(the_list: list, reverse: bool = False) -> tuple:
    """
        NAME
            bubblesort_2
        DESCRIPTION
            Sort a list of numbers in increasing order using a
            somewhat optimised version of bubblesort.
        RETURNS
            Returns a tuple consisting of
            1. The sorted list
            2. Number of swaps made during the sorting
            3. Number of comparisons made
        DATE
            2025-04-01
    """
    list_copy = the_list.copy()
    done = False
    ncomps, nswaps = 0, 0
    # Stop when done, i.e. no swaps have been made.
    # This should speed up the algorithm somewhat
    # compared to 'standard' bubblesort.
    while not done:
        done = True
        for index in range(len(list_copy) - 1):
            ncomps += 1
            if list_copy[index] > list_copy[index + 1]:
                done = False
                nswaps += 1
                (list_copy[index],
                 list_copy[index + 1]) = (list_copy[index + 1],
                                          list_copy[index])
    if reverse:
        return (list_copy[::-1], ncomps, nswaps)
    return (list_copy, ncomps, nswaps)


def bubblesort_2_2(the_list: list, reverse: bool = False) -> tuple:
    """
        NAME
            bubblesort_2_2
        DESCRIPTION
            Sort a list of numbers in increasing order using a
            somewhat optimised version of bubblesort.
                This version does not make a copy of the list
            it gets as an argument, so the original list
            will be sorted making the original, unsorted list
            unavailable for comparison... 
                NOTE: The calling code still expects the 
            (now sorted) list as the first element in the 
            returned tuple.
        RETURNS
            Returns a tuple consisting of
            1. The sorted list
            2. Number of swaps made during the sorting
            3. Number of comparisons made
        DATE
            2025-04-01
    """
    done = False
    ncomps, nswaps = 0, 0
    # Stop when done, i.e. no swaps have been made.
    # This should speed up the algorithm somewhat
    # compared to 'standard' bubblesort.
    while not done:
        done = True
        for index in range(len(the_list) - 1):
            ncomps += 1
            if the_list[index] > the_list[index + 1]:
                done = False
                nswaps += 1
                (the_list[index],
                 the_list[index + 1]) = (the_list[index + 1],
                                          the_list[index])
    if reverse:
        return (the_list[::-1], ncomps, nswaps)
    return (the_list, ncomps, nswaps)


def bubblesort(the_list: list, reverse: bool = False) -> tuple:
    """Another bubblesort implementation (slower)"""
    list_copy = the_list.copy()
    nswaps = 0
    ncomps = 0
    for _ in range(len(list_copy)):
        for index in range(len(list_copy) - 1):
            ncomps += 1
            if list_copy[index] > list_copy[index + 1]:
                nswaps += 1
                (list_copy[index],
                 list_copy[index + 1]) = (list_copy[index + 1],
                                          list_copy[index])
    if reverse:
        return (list_copy[::-1], ncomps, nswaps)
    return (list_copy, ncomps, nswaps)


def bubblesort_3(the_list: list, reverse: bool = False) -> tuple:
    """Another bubblesort implementation"""
    list_copy = the_list.copy()
    nswaps = 0
    ncomps = 0
    for index_one in range(len(list_copy)):
        for index_two in range(len(list_copy) - 1):
            ncomps += 1
            if list_copy[index_one] > list_copy[index_two]:
                nswaps += 1
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                          list_copy[index_one])
    if reverse:
        return (list_copy[::-1], ncomps, nswaps)
    return (list_copy, ncomps, nswaps)
