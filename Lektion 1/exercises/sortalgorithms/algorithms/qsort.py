# coding: utf-8
"""
    NAME
        qsort
    DESCRIPTION
        The quicksort algorithm in various disguises.
    AUTHOR
        mier
    DATE
        2025-05-15
    REFERENCES
        Wikipedia: https://en.wikipedia.org/wiki/Quicksort

"""
__all__ = ["qsort", "qsort2",
           "qsort_iterative",
           "qsort_iterative2"]

# pylint: disable=multiple-statements
# xpylint: disable=import-error
# xpylint: disable=unused-import
# import ipdb
# xpylint: enable=import-error
# xpylint: enable=unused-import
import numpy as np

# Globals used to hold the number of
# comparisons and swaps made durint
# the sorting. Defined here (as globals)
# so there's les


def partition(arr: np.ndarray, lo: int, hi: int) -> tuple:
    """
        Partition the array arr and return the
        position of the pivot element

        parameters
        ----------
            arr : iterable, list or np.ndarray
                The array to be sorted
            lo : int
                Lower index, i.e. the index where
                the sorting should begin
            hi : int
                Upper (or end) index
        returns
        -------
            A triple consisting of the partition pivot (int), the number
            of comparisons, and the number of swaps made durint the
            partitioning.

        pseudocode
        ----------
        # Divides array into two partitions
        *algorithm* partition(A, lo hi) *is*
            # Choose the last element as the pivot
            pivot := A[hi]
        # Temporary pivot index
        i := lo
        for j := lo to hi - 1 do
            # If the current element is less than or equal to the pivot
            if A[j] <= pivot then
                # Swap the current element with the element at
                # the temporary pivot index
                swap A[i] with A[j]
                # Move the temporary pivot index forward
                i := i + 1

        # Swap the pivot with the last element
        swap A[i] with A[hi]
        return i // the pivot index
    """
    # Keep track of the number os comparisons and swaps
    # made during the partitionen
    stats = np.zeros(2)  # [ncomps, nswaps]
    # Temporary pivot index
    pivot_index: int = lo
    # Choose the last element as pivot
    pivot = arr[hi]
    for k in range(lo, hi):
        # Update number of comparisons (for-loops make
        # comparisons, too)
        stats[0] += 1  # ncomps
        # If current element is less than or equal
        # to the pivot
        if arr[k] <= pivot:
            # Swap current element with the element at the
            # temporary pivot index
            arr[k], arr[pivot_index] = arr[pivot_index], arr[k]
            # Move the temporary pivot index forward
            pivot_index += 1
            # Update number of comparisons and swaps
            stats += 1  # ncomps, nswaps
    # Lastly, swap the element at the temporary pivot
    # index with the last element
    arr[hi], arr[pivot_index] = arr[pivot_index], arr[hi]
    # nswaps += 1
    stats[1] += 1
    # Return the (now final) pivot index
    return (pivot_index, stats[0], stats[1])


def partition2(arr: np.ndarray, lo: int, hi: int) -> tuple:
    """
        Partition the array arr and return the
        position of the pivot element

        parameters
        ----------
            arr : iterable, list or np.ndarray
                The array to be sorted
            lo : int
                Lower index, i.e. the index where
                the sorting should begin
            hi : int
                Upper (or end) index
        returns
        -------
            A triple consisting of the partition pivot (int), the number
            of comparisons, and the number of swaps made durint the
            partitioning.

        pseudocode
        ----------
        # Divides array into two partitions
        *algorithm* partition(A, lo hi) *is*
            # Choose the last element as the pivot
            pivot := A[hi]
        # Temporary pivot index
        i := lo
        for j := lo to hi - 1 do
            # If the current element is less than or equal to the pivot
            if A[j] <= pivot then
                # Swap the current element with the element at
                # the temporary pivot index
                swap A[i] with A[j]
                # Move the temporary pivot index forward
                i := i + 1

        # Swap the pivot with the last element
        swap A[i] with A[hi]
        return i // the pivot index
    """
    # Keep track of the number os comparisons and swaps
    # made during the partitioning
    stats = np.zeros(2)  # [ncomps, nswaps]
    # Temporary pivot index
    pivot_index: int = lo
    # Median of three choice of pivot
    mid = int((lo + hi) / 2)
    if arr[mid] < arr[lo]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    if arr[hi] < arr[lo]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[mid] < arr[hi]:
        arr[mid], arr[hi] = arr[hi], arr[mid]
    # Update number of comparisons and swaps
    stats += 3  # ncomps, nswaps
    # Choose the last element as pivot
    pivot = arr[hi]
    for k in range(lo, hi):
        # Update number of comparisons (for-loops make
        # comparisons, too)
        stats[0] += 1  # ncomps
        # If current element is less than or equal
        # to the pivot
        if arr[k] <= pivot:
            # Update number of comparisons and swaps
            stats += 1  # ncomps, nswaps
            # Swap current element with the element at the
            # temporary pivot index
            arr[k], arr[pivot_index] = arr[pivot_index], arr[k]
            # Move the temporary pivot index forward
            pivot_index += 1
    # Lastly, swap the element at the temporary pivot
    # index with the last element
    arr[hi], arr[pivot_index] = arr[pivot_index], arr[hi]
    # Update number of comparisons
    # nswaps += 1
    stats[1] += 1  # nswaps
    # Return the (now final) pivot index
    return (pivot_index, stats[0], stats[1])


def qsort(arr: np.ndarray, lo: int, hi: int,
          copylist: bool = False,
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
        tuple(None, ncomps, nswaps)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.

        Pseudocode
        ----------
        // Sorts (a portion of) an array, divides it into partitions,
        // then sorts those
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
                // Move the left index to the right at least once and
                // while the element at the left index is less than the pivot
                do i := i + 1 while A[i] < pivot

                // Move the right index to the left at least once and while
                // the element at the right index is greater than the pivot
                do j := j - 1 while A[j] > pivot

                // If the indices crossed, return
                if i >= j then return j

                // Swap the elements at the left and right indices
                swap A[i] with A[j]

    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Count the number of comparisons and swaps
    stats = np.zeros(2)  # [ncomps, nswaps]
    # Make sure the indices are in correct order.
    # This also the condition for breaking the recursion (?)
    if lo >= hi or lo < 0:
        stats[0] += 2  # ncomps
        return None, stats[0], stats[1]
    # Partition the array and get the pivot index
    pivot_index, nc, ns = partition(arr, lo, hi)
    stats[0] += nc  # ncomps
    stats[1] += ns  # nswaps
    # Recursively sort the two sub-partitions.
    # NOTE that the element at the partition index
    # is not included here; this is because the partitioning
    # ensures that the pivot element is in its final position.
    _, ncomps_lower, nswaps_lower = qsort(arr, lo, pivot_index - 1)
    _, ncomps_upper, nswaps_upper = qsort(arr, pivot_index + 1, hi)
    # Update number of comparisons and swaps
    stats[0] += (ncomps_lower + ncomps_upper)
    stats[1] += (nswaps_lower + nswaps_upper)
    if reverse:
        arr = np.sort(arr)[::-1]
    return None, stats[0], stats[1]


def qsort2(arr: np.ndarray, lo: int, hi: int,
           copylist: bool = False,
           reverse: bool = False) -> tuple:
    """
        An implementation of Quicksort.
        Uses an optimised pivot-selection procedure.

        Parameters
        _________
        arr : array_like
              Array to be sorted.
        reverse : bool, optional
                  Defaults to False, in which case the array is
                  sorted in ascending order.

        Returns
        -------
        tuple(None, ncomps, nswaps)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.

        Pseudocode
        ----------
        // Sorts (a portion of) an array, divides it into partitions,
        // then sorts those
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
                // Move the left index to the right at least once and while
                // the element at the left index is less than the pivot
                do i := i + 1 while A[i] < pivot

                // Move the right index to the left at least once and while
                // the element at the right index is greater than the pivot
                do j := j - 1 while A[j] > pivot

                // If the indices crossed, return
                if i >= j then return j

                // Swap the elements at the left and right indices
                swap A[i] with A[j]

    """
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Count the number of comparisons and swaps
    stats = np.zeros(2)  # [ncomps, nswaps]
    # Make sure the indices are in correct order.
    # This also the condition for breaking the recursion (?)
    if lo >= hi or lo < 0:
        stats[0] += 2  # ncomps
        return None, stats[0], stats[1]
    # Partition the array and get the pivot index
    (pivot_index, nc, ns) = partition2(arr, lo, hi)
    stats[0] += nc  # ncomps
    stats[1] += ns  # nswaps
    # Recursively sort the two sub-partitions.
    # NOTE that the element at the partition index
    # is not included here; this is because the partitioning
    # ensures that the pivot element is in its final position.
    _, ncomps_lower, nswaps_lower = qsort(arr, lo, pivot_index - 1)
    _, ncomps_upper, nswaps_upper = qsort(arr, pivot_index + 1, hi)
    # Update number of comparisons and swaps
    stats[0] += (ncomps_lower + ncomps_upper)  # ncomps
    stats[1] += (nswaps_lower + nswaps_upper)  # nswaps
    if reverse:
        arr = np.sort(arr)[::-1]
    return None, stats[0], stats[1]


def qsort_iterative(arr: np.ndarray, lo: int, hi: int,
                    copylist: bool = False,
                    reverse: bool = False) -> tuple:
    """
        Non-recursive (i.e. iterative) implementation of
        Quicksort.
        Uses an optimised pivot-selection procedure.

        Parameters
        _________
        arr : array_like
                Array to be sorted.
        lo, hi : int
                Lower and upper indices, defining a
                slice of the array, to be sorted.
        reverse : bool, optional
                Defaults to False, in which case the array is
                sorted in ascending order.
        Returns:
        -------
        tuple(None, ncomps, nswaps)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.

    """
    # pylint: disable=unused-variable
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Count the number of comparisons and swaps
    stats = np.zeros(2)  # [ncomps, nswaps]
    # Make sure the indices are in correct order.
    if lo >= hi or lo < 0:
        stats[0] += 2  # ncomps
        return None, stats[0], stats[1]
    # Create a stack where onto which we will push index-pointers
    # (successive values of 'lo' and 'hi').
    stack_size = hi - lo + 1  # Current length of the subarray
    stack = [0] * stack_size
    # stack = np.zeros(stack_size, dtype=np.int64)
    # Initialise the stack and push the current (initial) values
    # of 'lo' and 'hi' onto the stack.
    # Note that 'lo' and 'hi' are always pushed in that
    # order (and popped in the reverse order).
    stack[0] = lo  # top = 0
    stack[1] = hi  # top = 1
    top = 1
    # Loop while the stack's not empty by popping off
    # values of 'hi' and 'lo'
    while top >= 0:
        # Update number of comparisons
        stats[0] += 1  # ncomps
        # Pop hi and lo from the stack
        hi = stack[top]
        top -= 1
        lo = stack[top]
        top -= 1
        # Partition the current subarray (defined by the current
        # values of hi and lo). Get the current position of (the
        # index of) the pivot element, as chosen by partition().
        pivot_index, nc, ns = partition2(arr, lo, hi)
        # Update number of comparisons and swaps
        stats[0] += nc  # ncomps
        stats[1] += ns  # nswaps
        # If there are elements to the left of the pivot
        # element (i.e. if pivot is not at the beginning of the array?),
        # push the left side of the array onto the stack, to be
        # popped off in the iteration of the loop.
        if pivot_index > lo + 1:
            # Update number of comparisons
            stats[0] += 1  # ncomps
            # Push onto the stack (first lo, then hi)
            top += 1
            stack[top] = lo  # lo of the left-hand side
            top += 1
            stack[top] = pivot_index - 1  # hi of the left-hand side
        # If there are still elements to the right of the pivot
        # element (i.e. if pivot is not at the end of the array?),
        # push the right side of the array onto the stack, to be
        # popped off in the iteration of the loop.
        if pivot_index < hi - 1:
            # Update number of comparisons
            stats[0] += 1  # ncomps
            # Push onto the stack (first lo, then hi)
            top += 1
            stack[top] = pivot_index + 1  # lo of the right-hand side
            top += 1
            stack[top] = hi  # hi of the right-hand side
    if reverse:
        arr = np.sort(arr)[::-1]
    # Return a tuple of (<do_not_care_value>, <number of comparisons>,
    # <number of swaps>). The <do_not_care_value> is an artifact of the way
    # the performance-testing code collects data and could (should) be removed
    # from the code any-time-soon... Also, the number of 'swaps' does not
    # seem to be relevant for, at least, the quicksort code (should we instead
    # count number of assignments?)
    return None, stats[0], stats[1]


def qsort_iterative2(arr: np.ndarray, lo: int, hi: int,
                     copylist: bool = False,
                     reverse: bool = False) -> tuple:
    """
        Non-recursive (i.e. iterative) implementation of
        Quicksort.
        Uses an optimised pivot-selection procedure.
        Implements the stack with native list-methods
        (append(), pop()).

        Parameters
        _________
        arr : array_like
                Array to be sorted.
        lo, hi : int
                Lower and upper indices, defining a
                slice of the array, to be sorted.
        reverse : bool, optional
                Defaults to False, in which case the array is
                sorted in ascending order.
        Returns
        -------
        tuple(None, ncomps, nswaps)
            ncomps : int, number of comparisons made by the sorting algorithm.
            nswaps : int, number of swaps made by the sorting algorithm.

    """
    # pylint: disable=unused-variable
    if copylist:
        # Make a copy of the list
        arr = arr.copy()
    # Count the number of comparisons and swaps
    stats = np.zeros(2)  # [ncomps, nswaps]
    # Make sure the indices are in correct order.
    if lo >= hi or lo < 0:
        stats[0] += 2  # ncomps
        return None, stats[0], stats[1]
    # Create a stack onto which we will push and pop
    # successive values of 'lo' and 'hi'.
    stack: list = []
    # Initialise the stack and push the current (initial) values
    # of 'lo' and 'hi' onto the stack.
    # Note that 'lo' and 'hi' are always pushed in that
    # order (and popped in the reverse order).
    stack.append(lo)
    stack.append(hi)
    top: int = len(stack) - 1  # top <-- 1
    # Loop while the stack's not empty
    while top >= 0:
        # Update number of comparisons
        stats[0] += 1  # ncomps
        # Pop hi and lo from the stack
        hi = stack.pop()
        lo = stack.pop()
        top -= 2
        # Partition the current subarray (defined by the current
        # values of hi and lo). Get the current position of (the
        # index of) the pivot element, as chosen by partition().
        pivot_index, nc, ns = partition2(arr, lo, hi)
        # Update number of comparisons and swaps
        stats[0] += nc  # ncomps
        stats[1] += ns  # nswaps
        # If there are elements to the left of the pivot
        # (i.e. if pivot is not at the beginning of the array?),
        # push the left side of the array onto the stack.
        if pivot_index > lo + 1:
            # Update number of comparisons
            stats[0] += 1
            # Push onto the stack (first lo, then hi)
            stack.append(lo)  # lo of the left-hand side
            stack.append(pivot_index - 1)  # hi of the left-hand side
            top += 2
        # Push the right-hand side of the array onto the stack
        if pivot_index < hi - 1:
            # Update number of comparisons
            stats[0] += 1
            # Push onto the stack (first lo, then hi)
            stack.append(pivot_index + 1)  # lo of the right-hand side
            stack.append(hi)  # hi of the right-hand side
            top += 2
    if reverse:
        arr = np.sort(arr)[::-1]
    # Return a tuple of (<do_not_care_value>, <number of comparisons>,
    # <number of swaps>). The <do_not_care_value> is an artifact of the way
    # the performance-testing code collects data and could (should) be removed
    # from the code any-time-soon... Also, the number of 'swaps' does not
    # seem to be relevant for, at least, the quicksort code (should we instead
    # count number of assignments?)
    return None, stats[0], stats[1]
