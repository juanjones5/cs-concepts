"""
Deal with problems involving arrays containing numbers in a given range

For example, input is an array with nums in the range 1 to N:
[3,2,4,1]

For cyclic sort, we don't move index until we get the right element
for the index position

"""


def cyclic_sort(nums):
    """
    Time Complexity: O(N)
    Space: O(1)
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    return nums
