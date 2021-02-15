from typing import List

"""
SUBSET
Order does NOT matter
Each element could be absent or present
All possible combinations of all possible lengths, from 0 to n.

Time Complexity: O(2^N) Exponential
"""


def subsets(nums: List[int]) -> List[List[int]]:
    solution = []

    def backtrack(index, current):
        solution.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return solution


"""
COMBINATION
Like sub-sets for a given length
If we have `N` objects and we want to choose `k` of them:

Total combinations: `N! / K! (N - K)!`

"""


def combinations(n: int, k: int) -> List[List[int]]:
    solution = []

    def backtrack(index, current):
        if len(current) == k:
            solution.append(list(current))
            return
        for i in range(index, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return solution


"""
SUBSEQUENCE
Maintains order, can remove elements
Each element could be absent or present

Time Complexity: O(2 ^ N) Exponential
"""


def subsequences(nums: List[int]) -> List[List[int]]:
    solution = []

    def backtrack(index, current):
        solution.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return solution


"""
SUBARRAY / SUBSTRING
Contiguous subsequence, maintains order
Same array and empty array are considered

For each index, consider forward
N + (N - 1) + ... + 1 = (N * (N + 1)) // 2

Time Complexity: O(n^2)
"""
