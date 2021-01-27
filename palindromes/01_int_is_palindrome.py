"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward 
as forward. For example, 121 is palindrome while 123 is not.

https://leetcode.com/problems/palindrome-number/

Time Complexity: O(log10 N)
Space: O(1)
"""


def is_palindrome(num: int) -> bool:
    if num < 0 or (num % 10 == 0 and num != 0):
        return False
    reversed_num = 0
    while num > reversed_num:  # we only reverse half
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10
    return (num == reversed_num) or (
        num == reversed_num // 10
    )  # second case handles uneven number
