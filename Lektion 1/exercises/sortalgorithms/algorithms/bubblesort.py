# coding: utf-8
"""
    bubblesort.py

    Run with '-O' to get rid of debug messages:
    python -O bubblesort.py

"""
# pylint: disable=too-many-locals
# pylint: disable=consider-using-enumerate
### pylint: disable=too-many-statements

__all__ = ["bubblesort",
           "bubblesort_2",
           "bubblesort_3",
           "bubblesort_verbose"]

def bubblesort_2(the_list: list, reverse = False) -> tuple:
    """
    Sort a list of numbers in increasing order using bubblesort.

    Returns a tuple consisting of
        1. The sorted list
        2. Number of swaps made during the sorting
        3. Number of comparisons made
    """
    list_copy = the_list.copy()
    done = False
    no_swaps = 0
    no_comp = 0
    while not done:
        done = True
        for index in range(len(list_copy) - 1):
            no_comp += 1
            if list_copy[index] > list_copy[index + 1]:
                done = False
                no_swaps += 1
                (list_copy[index],
                 list_copy[index + 1]) = (list_copy[index + 1],
                                            list_copy[index])
    if reverse:
        return (list_copy[::-1], no_comp, no_swaps)
    return (list_copy, no_comp, no_swaps)



def bubblesort(the_list: list, reverse = False) -> tuple:
    """Another bubblesort implementation (slower)"""
    list_copy = the_list.copy()
    no_swaps = 0
    no_comp = 0
    for _ in range(len(list_copy)):
        for index in range(len(list_copy) - 1):
            no_comp += 1
            if list_copy[index] > list_copy[index + 1]:
                no_swaps += 1
                (list_copy[index],
                 list_copy[index + 1]) = (list_copy[index + 1],
                                      list_copy[index])
    if reverse:
        return (list_copy[::-1], no_comp, no_swaps)
    return (list_copy, no_comp, no_swaps)


def bubblesort_3(the_list: list, reverse = False) -> tuple:
    """Another bubblesort implementation"""
    list_copy = the_list.copy()
    no_swaps = 0
    no_comp = 0
    for index_one in range(len(list_copy)):
        for index_two in range(len(list_copy) - 1):
            no_comp += 1
            if list_copy[index_one] > list_copy[index_two]:
                no_swaps += 1
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                      list_copy[index_one])
    if reverse:
        return (list_copy[::-1], no_comp, no_swaps)
    return (list_copy, no_comp, no_swaps)


def bubblesort_verbose(the_list: list) -> tuple:
    """Bubblesort"""
    list_copy = the_list + []
    done = False
    no_swaps = 0
    no_comp = 0
    iteration = 1
    while not done:
        done = True
        print(f"iteration: {iteration}")
        for index in range(len(list_copy) - 1):
            no_comp += 1
            print(f"index: {index}:")
            print(f"{list_copy} ", end="")
            if list_copy[index] > list_copy[index + 1]:
                done = False
                no_swaps += 1
                print(f"---> ({index} > {index + 1}) swapped  <--- {list_copy}")
                (list_copy[index],
                 list_copy[index + 1]) = (list_copy[index + 1],
                                            list_copy[index])
            else:
                print(f"---> ({index} <= {index + 1}) no swap <--- {list_copy}")
        print()
        iteration += 1

    print(f"Number of comparisons: {no_comp}")
    print(f"Number of swaps: {no_swaps}")

    return (list_copy, no_comp, no_swaps)
