import math
from collections import defaultdict
from typing import List

"""
DYNAMIC SIZE SLIDING WINDOW PATTERN

K is not given, so the if statement inside the for
loop becomes a while loop, where we keep shrinking
the window until the condition is met,

In general, there are three variables to keep track:
- window_total (whatever is being calculated)
- window_start (start index)
- window_end (end index)

Constraints
1. If a wider scope of the sliding window is valid, the 
narrower scope of that wider scope is valid must hold.
2. If a narrower scope of the sliding window is invalid, the 
wider scope of that narrower scope is invalid must hold.
(this is why subarrays_with_given_sum cannot be solved)

Time Complexity: O(N)
Space: O(1)
"""


def smallest_subarray_with_given_sum(s, nums):
    """
    Length of the smallest contiguous subarray
    whose sum is greater than or equal to ‘s’
    """
    window_total, window_start = 0, 0
    min_len = math.inf
    for window_end in range(len(nums)):
        window_total += nums[window_end]
        while window_total >= s:
            min_len = min(min_len, window_end - window_start + 1)
            window_total -= nums[window_start]
            window_start += 1
    if min_len == math.inf:
        return 0
    return min_len


def subarrays_with_given_sum(s, nums):
    """
    Total number of continuous subarrays
    whose sum equals to k
    COUNTEREXAMPLE - SLIDING WINDOW DOES NOT WORK
    1st constraint does not hold, so we use
    a dictionary for prefix sums
    """
    cum_sum = result = 0
    # This dictionary will tell us from how many
    # elements in the array we have
    counter = defaultdict(int)
    # A 0 is needed to handle a case of having
    # a single element being equal to s
    counter[0] = 1
    for num in nums:
        cum_sum += num
        # if the needed number is not in the counter
        # we don't add to the result (i.e. we add 0)
        result += counter[cum_sum - s]
        # we might need the current cum_sum
        # to form a subarray later
        counter[cum_sum] += 1
    return result


def subarrays_with_product_less_than_k(k, nums):
    """
    Count subarrays where the product of all the
    elements in the subarray is less than k
    """
    if k <= 1:
        return 0
    window_start = result = 0
    window_total = 1
    for window_end in range(len(nums)):
        window_total *= nums[window_end]
        while window_total >= k:
            window_total /= nums[window_start]
            window_start += 1
        # all the subarrays of this subarray [window_start, window_end]
        # also meet the condition
        result += window_end - window_start + 1
    return result


def longest_substring_with_k_distinct(input_string, k):
    """
    Longest substring with no more than K distinct characters
    """
    longest_substring = 0
    window_start = 0
    char_freq = defaultdict(int)
    for window_end in range(len(input_string)):
        char_freq[input_string[window_end]] += 1
        while len(char_freq) > k:
            char_freq[input_string[window_start]] -= 1
            if char_freq[input_string[window_start]] == 0:
                del char_freq[input_string[window_start]]
            window_start += 1
        longest_substring = max(longest_substring, window_end - window_start + 1)
    return longest_substring


def non_repeat_substring(input_string):
    """
    Length of the longest substring with no repeating characters
    """
    max_len = 0
    window_start = 0
    char_index_map = {}
    for window_end in range(len(input_string)):
        right_char = input_string[window_end]
        if right_char in char_index_map:
            # in the current window, we will not have any 'right_char'
            # after its previous index, and if 'window_start' is already
            # ahead of the last index of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def min_sub_array_len(s: int, nums: List[int]) -> int:
    """
    Given an array of n positive integers and a positive
    integer s, find the minimal length of a contiguous
    subarray of which the sum ≥ s. If there isn't one,
    return 0 instead.
    Time Complexity: O(N)
    Space: O(1)
    """
    window_start = window_sum = 0
    solution = len(nums) + 1
    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        while window_sum >= s:
            solution = min(solution, window_end - window_start + 1)
            window_sum -= nums[window_start]
            window_start += 1
    return solution if solution < (len(nums) + 1) else 0