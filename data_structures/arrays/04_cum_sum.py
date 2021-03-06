from typing import List
from collections import defaultdict


def pivot_index(nums: List[int]) -> int:
    """
    Given an array of integers nums, write a method
    that returns the "pivot" index of this array.
    We define the pivot index as the index where the
    sum of all the numbers to the left of the index
    is equal to the sum of all the numbers to the
    right of the index
    Time Complexity: O(N)
    Space: O(1)
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    for j in range(0, len(nums)):
        right = nums[len(nums) - 1] - nums[j]
        left = nums[j - 1] if j > 0 else 0
        if left == right:
            return j
    return -1


def subarrays_with_given_sum(k: int, nums: List[int]) -> int:
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
        result += counter[cum_sum - k]
        # we might need the current cum_sum
        # to form a subarray later
        counter[cum_sum] += 1
    return result


def subarrays_with_sum_divisible_by(k: int, nums: List[int]) -> int:
    """
    Total number of continuous subarrays
    whose sum is divisible by k
    COUNTEREXAMPLE - SLIDING WINDOW DOES NOT WORK
    1st constraint does not hold, so we use
    a dictionary for prefix sums
    """
    counter = defaultdict(int)
    counter[0] = 1
    cum_sum = total = 0
    for num in nums:
        cum_sum += num
        total += counter[(cum_sum + k) % k]
        counter[cum_sum % k] += 1
    return total


def subarrays_with_sum_product_of(nums: List[int], k: int) -> bool:
    """
    Given a list of non-negative numbers and a target integer k,
    write a function to check if the array has a continuous subarray
    of size at least 2 that sums up to a multiple of k, that is,
    sums up to n*k where n is also an integer.
    """
    cusum = 0
    data = {0: -1}
    for i in range(len(nums)):
        cusum += nums[i]
        if k != 0:
            cusum = cusum % k
        if cusum in data:
            if (i - data[cusum]) >= 2:
                return True
        else:
            data[cusum] = i
    return False


def product_except_self(nums: List[int]) -> List[int]:
    """
    Given an array nums of n integers where n > 1,
    return an array output such that output[i] is equal
    to the product of all the elements of nums except nums[i]
    Time Complexity: O(N)
    Space: O(1) not counting output array
    """
    res = [nums[0]]
    for i in range(1, len(nums)):
        res.append(res[-1] * nums[i])
    for j in range(len(nums) - 1)[::-1]:
        nums[j] *= nums[j + 1]
    for i in range(len(nums))[::-1]:
        left = res[i - 1] if i > 0 else 1
        right = nums[i + 1] if i < len(nums) - 1 else 1
        res[i] = left * right
    return res