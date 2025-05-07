# coding: utf-8
"""
    bubblesort.py

    Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
# pylint: disable=consider-using-enumerate

__all__ = ["bubblesort",
           "bubblesort_nocopy",
           "bubblesort2",
           "bubblesort2_nocopy",
           "bubblesort3",
           "bubblesort3_nocopy"]


def bubblesort(the_list: list, reverse: bool = False) -> tuple:
    """Vanilla bubblesort"""
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


def bubblesort_nocopy(the_list: list, reverse: bool = False) -> tuple:
    """Vanilla bubblesort"""
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


def bubblesort2(the_list: list, reverse: bool = False) -> tuple:
    """
        NAME
            bubblesort2
        DESCRIPTION
            Bubblesort somewhat optimised: returns when no
            swaps have been done.
            Default is to sort in increasing order.
        PARAMETERS
            the_list : list of numbers to be sorted
            reverse : bool

        RETURNS
            Returns a tuple consisting of
            1. The a sorted copy of the list
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


def bubblesort2_nocopy(the_list: list, reverse: bool = False) -> tuple:
    """
        NAME
            bubblesort2_2
        DESCRIPTION
            Bubblesort somewhat optimised: returns when no
            swaps have been done.
           Default is to sort in increasing order.
           Same as bubblesort2() except no copy of the list
            is made.
        PARAMETERS
            the_list : list of numbers to be sorted
            reverse : bool

        RETURNS
            Returns a tuple consisting of
            1. The a sorted copy of the list
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


def bubblesort3(the_list: list, reverse: bool = False) -> tuple:
    """Another bubblesort implementation, or rather insertionsort(?)..."""
    list_copy = the_list.copy()
    nswaps = 0
    ncomps = 0
    for index_one in range(len(list_copy)):
        for index_two in range(len(list_copy) - 1):
            ncomps += 1
            if list_copy[index_one] < list_copy[index_two]:
                nswaps += 1
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                          list_copy[index_one])
    if reverse:
        return (list_copy[::-1], ncomps, nswaps)
    return (list_copy, ncomps, nswaps)


def bubblesort3_nocopy(the_list: list, reverse: bool = False) -> tuple:
    """Another bubblesort implementation, or rather insertionsort(?)...
       Same as bubblesort3 but no copy is made """
    nswaps = 0
    ncomps = 0
    for index_one in range(len(the_list)):
        for index_two in range(len(the_list) - 1):
            ncomps += 1
            if the_list[index_one] < the_list[index_two]:
                nswaps += 1
                (the_list[index_one],
                 the_list[index_two]) = (the_list[index_two],
                                          the_list[index_one])
    if reverse:
        return (the_list[::-1], ncomps, nswaps)
    return (the_list, ncomps, nswaps)
