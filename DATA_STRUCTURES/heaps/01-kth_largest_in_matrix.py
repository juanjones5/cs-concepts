import heapq
from typing import List

"""
Given a n x n matrix where each of the rows 
and columns are sorted in ascending order, 
find the kth smallest element in the matrix.
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return heapq.nsmallest(
            k, [row[i] for row in matrix for i in range(min(len(row), k))]
        )[-1]
