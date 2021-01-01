"""
Given a non-empty string s and a dictionary wordDict 
containing a list of non-empty words, determine if s 
can be segmented into a space-separated sequence of 
one or more dictionary words.

The same word in the dictionary may be reused multiple 
times in the segmentation. You may assume the dictionary 
does not contain duplicate words.

"""
from typing import List

class Solution:
    def solve(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
