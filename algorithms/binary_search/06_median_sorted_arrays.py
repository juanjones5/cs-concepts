"""
Given two sorted arrays nums1 and nums2 of size m and n 
respectively, return the median of the two sorted arrays.

Time Complexity: O(min(m, n))
Space: O(1)
"""

from typing import List


def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A
    total_len = len(A) + len(B)
    partition_len = total_len // 2
    lo, hi = 0, len(A) - 1
    while True:
        A_idx = lo + (hi - lo) // 2
        B_idx = (partition_len - 1) - (A_idx + 1)

        A_left = A[A_idx] if A_idx >= 0 else float("-inf")
        A_right = A[A_idx + 1] if A_idx + 1 < len(A) else float("inf")
        B_left = B[B_idx] if B_idx >= 0 else float("-inf")
        B_right = B[B_idx + 1] if B_idx + 1 < len(B) else float("inf")

        # Check if we found the right partition
        if A_left <= B_right and B_left <= A_right:
            # Median for odd
            if total_len % 2 > 0:
                return min(A_right, B_right)
            # Median for even
            else:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2

        # Continue Binary Search
        if B_left > A_right:
            lo = A_idx + 1
        else:
            hi = A_idx - 1