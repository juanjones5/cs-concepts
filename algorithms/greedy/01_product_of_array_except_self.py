"""
Given an array nums of n integers where n > 1,  
return an array output such that output[i] 
is equal to the product of all the elements 
of nums except nums[i].
"""


def product_of_array_except_self(nums):
    result = [1]
    # 1. Populate the array with the products to the left
    for i in range(1, len(nums)):
        result.append(nums[i - 1] * result[i - 1])
    right = 1
    # 2. From the end of that array,
    # multiply each index by the products to the right
    for j in reversed(range(len(nums))):
        result[j] = result[j] * right
        right *= nums[j]
    return result