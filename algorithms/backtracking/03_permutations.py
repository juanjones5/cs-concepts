"""
PERMUTATIONS
We care about the order of the elements and we
use all the elements.
A permutation is essentially an ordered combination, 
except the total length of each permutation must 
equal the original input.

There are two types of permutation: 
with repetition & without repetition

i.e. 1234 and 4321 are different permutations

Total elements: N!
"""

from typing import List


def permutations(nums: List[int]) -> List[List[int]]:
    """
    Return ALL possible permutations of nums
    in any order.
    Time Complexity: O(N!)
    Space: O(N!)
    """
    solution = []

    def backtrack(index):
        # BASE CASE - GOAL
        if index == len(nums):
            # IMPORTANT, create copy
            # when mutating recursively
            solution.append(list(nums))
        for i in range(index, len(nums)):
            # Here we can just modify nums instead of having
            # an extra array for the current_solution
            nums[index], nums[i] = nums[i], nums[index]
            # Calling using index + 1 ensures that
            # each branch will have the same amount of leaves
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    backtrack(0)
    return solution