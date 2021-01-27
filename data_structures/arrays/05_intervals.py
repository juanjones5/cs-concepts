"""
MERGE INTERVALS PATTERN

This pattern describes an efficient technique to deal with 
overlapping intervals. In a lot of problems involving intervals, 
we either need to find overlapping intervals or merge intervals 
if they overlap.

Sort Intervals by start time.

Time Complexity: O(N log N) for sorting
Space: O(N) in Python for sorting
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    # 1. Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    for interval in intervals:
        # If current start time is bigger than
        # previous end time, it is a different interval
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        # Otherwise, they overlap and we use the latest
        # end time among the two of them
        else:  # they overlap
            result[-1][1] = max(result[-1][1], interval[1])
    return result


def interval_intersection(
    self, A: List[List[int]], B: List[List[int]]
) -> List[List[int]]:
    """
    You are given two lists of closed intervals where
    A[i] = [starti, endi] and B[j] = [startj, endj]
    Each list of intervals is pairwise disjoint and in sorted order

    Return the intersection of these two interval lists

    Time Complexity: O(m + n)
    Space: O(m + n)
    """
    ans = []
    i = j = 0
    while i < len(A) and j < len(B):
        lo = max(A[i][0], B[j][0])
        hi = min(A[i][1], B[j][1])
        if lo <= hi:
            ans.append([lo, hi])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return ans


def can_attend_all_appointments(intervals):
    """
    Given an array of intervals representing ‘N’ appointments,
    find out if a person can attend all the appointments.
    """
    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i - 1][end]:
            return False
    return True
