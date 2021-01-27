"""
SUBSETS
Input an array without duplicate numbers, 
and your algorithm needs to output all 
subsets of these numbers
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Return all possible subsets of nums
    Time Complexity: O(N * 2^N)
    Space: O(N * 2^N)
    """
    solution = []

    def backtrack(index=0, current=[]):
        solution.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            # Calling using i + 1 makes that
            # our first branch is [1,2] and [1,3]
            backtrack(i + 1, current)
            current.pop()

    backtrack()
    return solution