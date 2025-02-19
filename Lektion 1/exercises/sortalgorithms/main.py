"""
2025-02-19
sortalgorithms.py

Uses bubblesort and a modified version
of that algorithm to sort lists of numbers.
"""

from algorithms.performance import timeIt
from algorithms.performance import algorithmPerformance
from algorithms.defaults import ITERATIONS


def main() -> None:
    """main"""
    # Measure execution time
    timeIt()
    # Measure performance in terms of (mean) number of
    # swaps and (mean) number of comparisons
    (meanNumberOfSwaps,
     meanNumberOfComparisons) = algorithmPerformance(
         iterations=ITERATIONS)
###     # Print results
###     print(f"list-length: {N}, iterations: {ITERATIONS}")
###     print(f"Mean number of swaps: {meanNumberOfSwaps}")
###     print(f"Mean number of comparisons: {meanNumberOfComparisons}")
### 
###     # Sort and display once to make verify that the algorithm works
###     ## randomNumbers = generateRandomList(MIN, MAX, N, verbose=False)
###     # Sort the list and collect statistics
###     ## (sortedRandomNumbers, _, _) = mySortAlgorithm(randomNumbers, verbose=False)
###     ## print(f"in = {randomNumbers}")
###     ## print(f"out = {sortedRandomNumbers}")


if __name__ == "__main__":
    main()
