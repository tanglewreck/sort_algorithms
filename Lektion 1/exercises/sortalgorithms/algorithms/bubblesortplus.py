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

__all__ = ["bubblesort_plus", "bubblesort_plus_verbose"]

# pylint: disable=invalid-name

#def switchPlace(the_list: list, positionOne: int, positionTwo: int) -> None:
#    """
#    Utility function that swaps places of two elements.
#    The position of the elements are given by the (integer)
#    parameters 'positionOne' and 'positionTwo.
#
#    NOTE that using this function implies a performance hit
#    as  compared to doing the swap inline. The code is
#    preserved as a reminder of this.
#    """
#    try:
#        the_list[positionOne], the_list[positionTwo] = the_list[positionTwo], the_list[positionOne]
#    except IndexError as e:
#        print(f"Got an IndexError: {e}")


def bubblesort_plus(the_list: list, reverse = False) -> tuple:
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

    # Repeatedly iterate through the list of numbers, compare the first element with
    # the rest of the elements in turn, switching places if the first is larger
    # than the other element, thus forcing the smallest element of the list to
    # the head.
    #
    # Since, in each iteration, the smallest number is moved to the head of the
    # list in this way, we can optimise by ignoring those numbers we have
    # already moved.
    #
    # Another way of putting this is that the list elements that are moved to
    # the beginning of the list are all in their correct position, so we can ignore
    # those elements as we progress further down the list.

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


def bubblesort_plus_verbose(the_list: list) -> tuple:
    """
    Verbose, otherwise same as above
    """
    # Store the length of the list in a variable, for easy access
    list_len: int = len(the_list)

    # We count the number of comparisons and swaps made
    no_comp = 0
    no_swaps = 0

    # Make a copy of the list and sort this instead of the original
    # so we can compare input and output.
    list_copy = the_list + []

    # Repeatedly iterate through the list of numbers, compare the first element with
    # the rest of the elements in turn, switching places if the first is larger
    # than the other element, thus forcing the smallest element of the list to
    # the head.
    #
    # Since, in each iteration, the smallest number is moved to the head of the
    # list in this way, we can optimise by ignoring those numbers we have
    # already moved (the 'firstIndex' variable keeps track of this).
    #
    # Another way of putting this is that the list elements that are moved to
    # the beginning of the list are all in their correct position, so we can ignore
    # those elements as we progress further down the list.

    # The variable 'firstIndex' is incremented by one with each
    # iteration of the loop, making the list of numbers
    # to compare shorter for (almost) every run of the loop.
    firstIndex = 0

    for index_one in range(firstIndex, list_len):
        print(f"interation: {index_one} (firstIndex = {firstIndex})")
        for index_two in range(index_one + 1, list_len):  # loop from index_one to list_len -1
            print(f"{list_copy}\t", end="")

            no_comp += 1
            if list_copy[index_one] > list_copy[index_two]:
                print(f"---> ({list_copy[index_one]} > {list_copy[index_two]}) swapped  <--- ",
                      end="")
                # Make the swap
                (list_copy[index_one],
                 list_copy[index_two]) = (list_copy[index_two],
                                          list_copy[index_one])
                no_swaps += 1
            else:
                print(f"---> ({list_copy[index_one]} <= {list_copy[index_two]}) "
                       "no swap  <--- ", end="")
            print(list_copy)
        print()
        firstIndex += 1

    print(f"Number of comparisons: {no_comp}")
    print(f"Number of swaps: {no_swaps}")

    return (list_copy, no_comp, no_swaps)
