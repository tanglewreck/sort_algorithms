# coding: utf-8
def inssort(arr):
     # PSEUDOCODE
     # i ← 1
     # while i < length(A)
     # x ← A[i]
     # j ← i
     # while j > 0 and A[j-1] > x
     #     A[j] ← A[j-1]
     #     j ← j - 1
     # end while
     # A[j] ← x
     # i ← i + 1
     # end while
     ncomps, nswaps = 0, 0
     arr_copy = arr.copy()
     i = 1
     while i < len(arr_copy):
         x = arr_copy[i]
         j = i
         while j > 0 and arr_copy[j-1] > x:
             ncomps += 2
             nswaps += 1
             arr_copy[j] = arr_copy[j-1]
             j = j - 1
         nswaps += 1  
         arr_copy[j] = x
         i += 1
     return arr_copy, ncomps, nswaps
