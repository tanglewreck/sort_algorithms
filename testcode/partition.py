# coding: utf-8
"""
    NAME
        partition
    AUTHOR
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
