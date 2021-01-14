"""
TWO POINTERS PATTERN

For sorted arrays or LinkedLists where we need to 
find a set of elements (tuple, triplet, subarray) 
that fulfill certain constraints

"""


def pair_with_target_sum(nums, target_sum):
    """
    LEFT & RIGHT pointer example
    TWO SUM II (Array is sorted)
    Pair in sorted array whose sum is equal to the given target
    Time Complexity: O(N)
    Space: O(1)

    Note: if the array wasn't sorted (TWO SUM I), it is better to
    use a dict where the key is the nums[i] and the value is i
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < target_sum:
            left += 1
        elif current_sum > target_sum:
            right -= 1
        else:
            return [left, right]
    return [-1, -1]


def subsequence_count_with_target_sum(nums, target_sum):
    """
    LEFT & RIGHT pointer example
    Given an array of integers nums and an integer target.
    Number of non-empty subsequences of unsorted nums such
    that the sum of the minimum and maximum element on it
    is less or equal to target.
    Since the answer may be too large, return it modulo 10**9+7
    Time Complexity: O(N log N) for sorting
    Space: O(N) for sorting
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    solution = 0
    mod = 10 ** 9 + 7
    while left <= right:  # <= because it could be a sinle element
        current_sum = nums[left] + nums[right]
        if current_sum <= target_sum:
            nums_inside = right - left
            solution += pow(2, nums_inside, mod)
            left += 1
        else:
            right -= 1
    return solution % mod


def squaring_sorted_array(nums):
    """
    LEFT & RIGHT pointer example
    Return sorted squares of each number in sorted array
    nums might contain negative numbers
    Time Complexity: O(N)
    Space: O(N)
    """
    squares = [0] * len(nums)
    highest_index = len(nums) - 1
    left, right = 0, len(nums) - 1
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if right_square > left_square:
            squares[highest_index] = right_square
            right -= 1
        else:
            squares[highest_index] = left_square
            left += 1
        highest_index -= 1
    return squares


def triplets_with_zero_sum(nums):
    """
    THREE POINTER: FROM_INDEX + LEFT & RIGHT
    THREE SUM
    Given unsorted numbers, find all unique triplets
    in it that add up to zero
    Time Complexity: O(N^2)
    Space: O(N) required for sorting
    """
    # 1. Sort nums
    nums.sort()
    triplets = []
    # 2. Two pointer calculation from every index
    for i in range(len(nums)):
        # 3. Avoid processing duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target_sum = -nums[i]
        # 4. Traditional LEFT & RIGHT pointer from i
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target_sum:
                triplets.append([-target_sum, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1  # skip same element to avoid duplicate triplets
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  # skip same element to avoid duplicate triplets
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
    return triplets


def remove_duplicates(nums):
    """
    NEXT INDEX pointer example
    Remove all duplicates from sorted array in-place
    Time Complexity: O(N)
    Space: O(1)
    """
    next_non_duplicate = 1
    i = 1
    while i < len(nums):
        if nums[next_non_duplicate - 1] != nums[i]:
            nums[next_non_duplicate] = nums[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate


def merge_sorted_array(nums1, m, nums2, n):
    """
    THREE POINTERS REVERSING
    Given two sorted integer arrays nums1 and nums2,
    merge nums2 into nums1 as one sorted array
    Time Complexity: O(N)
    Space: O(1)
    """
    main_ptr = m + n - 1
    nums1_ptr = m - 1
    nums2_ptr = n - 1
    while nums1_ptr >= 0 and nums2_ptr >= 0:
        if nums1[nums1_ptr] > nums2[nums2_ptr]:
            nums1[main_ptr] = nums1[nums1_ptr]
            nums1_ptr -= 1
        else:
            nums1[main_ptr] = nums2[nums2_ptr]
            nums2_ptr -= 1
        main_ptr -= 1
    # in case there are numbers left in nums2
    # after we moved all the numbers from nums1
    nums1[: nums2_ptr + 1] = nums2[: nums2_ptr + 1]


def is_subsequence(s: str, t: str) -> bool:
    """
    TWO POINTERS, ONE FOR EACH ARRAY
    Given a string s and a string t,
    check if s is subsequence of t
    Time Complexity: O(N)
    Space: O(1)
    """
    s_ptr = t_ptr = 0
    while s_ptr < len(s) and t_ptr < len(t):
        if s[s_ptr] == t[t_ptr]:
            s_ptr += 1
        t_ptr += 1
    return s_ptr == len(s)
