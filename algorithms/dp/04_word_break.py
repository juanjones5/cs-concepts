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
from collections import defaultdict


def word_break_memo(s: str, wordDict: List[str]) -> bool:
    memo = defaultdict(lambda: None)

    def rec(current):
        if not len(current):
            return True
        if memo[current] is not None:
            return memo[current]
        for word in wordDict:
            if current.endswith(word):
                if rec(current[: len(current) - len(word)]):
                    memo[current] = True
                    return True
        memo[current] = False
        return False

    return rec(s)


def word_break_dp(s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(0, i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
    return dp[len(s)]


def word_break_all_possibilities(s: str, wordDict: List[str]) -> List[str]:
    memo = defaultdict(list)

    def rec(string):
        if not string:
            return [[]]
        if string in memo:
            return memo[string]
        for word in wordDict:
            if string.startswith(word):
                res = rec(string[len(word) :])
                for r in res:
                    memo[string].append([word] + r)
        return memo[string]

    rec(s)
    return [" ".join(words) for words in memo[s]]
