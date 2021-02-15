"""
SUBSETS
Input an array without duplicate numbers, 
and your algorithm needs to output all 
subsets of these numbers
"""

from typing import List
from collections import defaultdict


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


def remove_invalid_parentheses(s: str) -> List[str]:
    """
    Remove the minimum number of invalid parentheses in order to
    make the input string valid. Return all possible results.

    Note: The input string may contain letters other than
    the parentheses ( and ).

    Time Complexity: O(2^N)
    Space
    """
    solution = defaultdict(set)
    max_len = 0
    current = []

    def backtrack(index=0, l_count=0, r_count=0):
        nonlocal max_len
        n = len(current)
        if l_count == r_count and n >= max_len:
            max_len = max(max_len, n)
            solution[n].add("".join(current))
        for i in range(index, len(s)):
            if l_count == r_count and s[i] == ")":
                continue
            current.append(s[i])
            new_l = l_count + (1 if s[i] == "(" else 0)
            new_r = r_count + (1 if s[i] == ")" else 0)
            backtrack(i + 1, new_l, new_r)
            current.pop()

    backtrack()
    return solution[max_len]