"""
KADANE'S ALGORITHM
"""


def max_sum_subarray(nums):
    """
    Contiguous subarray with the largest
    sum and return its sum
    Time Complexity: O(N)
    Space: O(1)
    """
    if not nums:
        return 0
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


def max_product_subarray(nums):
    """
    Contiguous subarray with the largest
    product and return its product
    Time Complexity: O(N)
    Space: O(1)
    """
    if not nums:
        return 0
    current_min_product = current_max_product = max_product = nums[0]
    for i in range(1, len(nums)):
        # we keep current_min_product in case it is negative and nums[i]
        # is negative as well, giving a positive current_max_product
        temp_max = max(
            current_max_product * nums[i], current_min_product * nums[i], nums[i]
        )
        current_min_product = min(
            current_max_product * nums[i], current_min_product * nums[i], nums[i]
        )
        current_max_product = temp_max
        max_product = max(current_max_product, max_product)
    return max_product
