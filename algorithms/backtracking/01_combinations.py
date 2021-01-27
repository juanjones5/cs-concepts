"""
COMBINATIONS
We DO NOT care about the order of the elements.
Two combinations are unique if the frequency
of at least one of the chosen numbers is different
i.e. 1234 and 4321 are the same combination

If we have `N` objects and we want to choose `k` of them:

Total combinations: `N! / K! (N - K)!`
"""

from typing import List
from collections import Counter


def combinations(self, n: int, k: int) -> List[List[int]]:
    """
    Return all possible combinations of k numbers out of 1 ... n
    """
    solution = []
    current_solution = []

    def backtrack(index: int = 1):
        # BASE CASE - GOAL
        if len(current_solution) == k:
            solution.append(list(current_solution))
            return
        for i in range(index, n + 1):
            current_solution.append(i)
            # Calling using i + 1 makes that
            # our first branch is [1,2] and [1,3]
            backtrack(i + 1)
            current_solution.pop()

    backtrack()
    return solution


def combination_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Return a list of all unique combinations of nums where the
    chosen numbers sum to target.

    The same number may be chosen from candidates an unlimited
    number of times. Two combinations are unique if the frequency
    of at least one of the chosen numbers is different.
    """
    solution = []
    current_solution = []

    def backtrack(index=0, current_sum=0):
        # TWO BASE CASES, we exceeded the target or we found it
        if current_sum > target:
            return
        if current_sum == 0:
            # IMPORTANT MAKE A DEEP COPY OF THE CURRENT
            solution.append(list(current_solution))
            return
        for i in range(index, len(nums)):
            current_solution.append(nums[i])
            # We call using `i` instead of `i+1`
            # because we are allowed to use repetitions
            backtrack(i, current_sum + nums[i])
            # BACKTRACK CURRENT SOLUTION
            current_solution.pop()

    backtrack()
    return solution


def combination_sum_ii(nums: List[int], target: int) -> List[List[int]]:
    """
    Given a collection of candidate numbers (candidates) and a target
    number (target), find all unique combinations in candidates where
    the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.
    Time Complexity: O(2 ^ N)
    Space Complexity: O(N) if we do not count the input array
    """
    solution = []
    current_solution = []
    counter = Counter(nums)
    counter = [(num, freq) for num, freq in counter.items()]

    def backtrack(index=0, current_sum=0):
        if current_sum > target:
            return
        if current_sum == target:
            solution.append(list(current_solution))
            return
        for i in range(index, len(counter)):
            element, freq = counter[i]
            # constraint
            if freq <= 0:
                continue
            # change
            current_solution.append(element)
            counter[i] = (element, freq - 1)
            # recursive call
            backtrack(i, current_sum + element)
            # backtrack
            counter[i] = (element, freq)
            current_solution.pop()

    backtrack()
    return solution