"""
LENGH OF LONGEST INCREASING SUBSEQUENCE

A subsequence is different than a substring
In a subsequence we can skip some element of the array

1. Define subproblem in words
dp[i] = length of LIS on a1, a2, ..., ai WHICH INCLUDES ai

2. State recursive relation

dp[i] = 1 + max(value(keys bigger than i))
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [1] * len(nums)
        for i in range(len(dp)):
            max_value = 0
            for j in range(0, i):
                if nums[j] < nums[i] and dp[j] > max_value:
                    max_value = dp[j]
            dp[i] = dp[i] + max_value
        return max(dp)