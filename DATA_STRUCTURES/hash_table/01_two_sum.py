"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:

    def solve(self, nums, target):
        data = {}
        for i in range(len(nums)):
            if nums[i] in data:
                return [i, data[nums[i]]]
            data[target - nums[i]] = i
        return []

    # if the list is sorted, use pointers:
    def solve_sorted(self, numbers, target):
        if numbers is None or len(numbers) == 0:
            return []
        left, right = 0, len(numbers) - 1
        while left <= right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        return []