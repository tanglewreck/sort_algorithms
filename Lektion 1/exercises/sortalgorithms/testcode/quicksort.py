# coding: utf-8
"""
    NAME
        quicksort
    Author
        mier
    DATE
        2025-05-15

"""


def partition(arr, lo:int, hi: int) -> int:
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
            The index of the partition pivot
        """
    # Choose the last element as pivot
    pivot = arr[hi]
    # Temporary pivot index
    piv_ind = lo
    for k in range(lo, hi):
        # If current element is less than or equal
        # to the pivot
        if arr[k] <= pivot:
            # Swap current element with the element at the
            # temporary pivot index
            arr[k], arr[piv_ind] = arr[piv_ind], arr[k]
            # Move the temporary pivot index forward
            piv_ind += 1
    # Lastly, swap the element at the temporary pivot
    # index with the last element
    arr[hi], arr[piv_ind] = arr[piv_ind], arr[hi]
    # Return the (now final) pivot index
    return piv_ind


def quicksort(arr, lo, hi):
    """
        Sorts (a partition of) an array; divides it into
        partitions, and then (recursively) sorts those.

        If arr is the array to be sorted, the initial call
        should be 'quicksort(arr, 0, len(arr) - 1'.

        The sorting is done inline, i.e. the sorting takes
        places within the array itself; save a copy of the
        array if you want to compare the original to the
        sorted array.

        Adapted to Python from the pseudocode in the Wikipedia
        article on Quicksort (https://en.wikipedia.org/wiki/Quicksort).

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
           tuple
    """
    # Make sure the indices are in correct order.
    # This also the condition for breaking the recursion (?)
    if lo >= hi or lo < 0:
        if __debug__:
            print("Breaking the recursion: ", end="")
            if lo >= hi:
                print(f" lo ≥ hi: lo={lo}, hi={hi}")
            if lo < 0:
                print(f" lo < 0:  lo={lo}")
        return (None, None, None)
    # Partition the array and get the pivot index
    pivot_index = partition(arr, lo, hi)
    if __debug__:
        print(f"pivot_index = {pivot_index}")
        print(f"lo partition = arr[{lo}:{pivot_index -1}] = "
              f"{arr[lo: pivot_index - 1]}")
        print(f"hi partition = arr[{pivot_index + 1}:{hi}] = "
              f"{arr[pivot_index + 1:hi]}")
    # Recursively sort the two sub-partitions.
    # NOTE that the element at the partition index
    # is not included here; this is because the partitioning
    # ensures that the pivot element is in its final position.
    quicksort(arr, lo, pivot_index - 1)
    quicksort(arr, pivot_index + 1, hi)
    return (arr, 0, 0)


if __name__ == "__main__":
    pass
