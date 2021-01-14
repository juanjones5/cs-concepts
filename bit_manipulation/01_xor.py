"""
Bitwise XOR Pattern
"""

from typing import List


def find_single_number(nums: List[int]) -> int:
    """
    Every number appears twice except for one, find that single number.
    Time complexity: O(N)
    Space: O(1) This would be O(N) if we use a hash map
    """
    num = 0
    for i in nums:
        num ^= i
    return num


def find_single_numbers(nums):
    """
    Every number appears exactly twice except two numbers that
    appear only once. Find the two numbers that appear only once
    Time complexity: O(N)
    Space: O(1) This would be O(N) if we use a hash map
    """
    # 1. get the XOR of the all the numbers
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    # 2. get the rightmost bit that is '1'
    # that means that n1 and n2 must be
    # different on that bit
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1

    # 3. split all nums in by having this bit
    # 'rightmost_set_bit' set or not
    num1, num2 = 0, 0
    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]
