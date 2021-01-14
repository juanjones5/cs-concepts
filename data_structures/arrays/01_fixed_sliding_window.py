"""
SLIDING WINDOW PATTERN

When dealing with an array or a LinkedList, and we 
are asked to find or calculate something among all the 
CONTIGUOUS SUBARRAYS (or sublists) of a given size.

The idea is to reuse the overlapping calculations of
contiguous k-sized windows.

In general, there are three variables to keep track:
- window_total (whatever is being calculated)
- window_start (start index)
- window_end (end index)

Time Complexity: O(N)
Space: O(1)
"""


def find_averages_of_subarrays(k, nums):
    """
    Average of all contiguous subarrays of size 'k'
    """
    result = []
    window_sum, window_start = 0, 0
    # 1. For all possible window ends
    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        # 2. Check if valid window
        if window_end >= (k - 1):
            # 3. Calculation for current window
            result.append(window_sum / k)
            # 4. Subtract element leaving window
            window_sum -= nums[window_start]
            # 5. Slide window forward
            window_start += 1
    return result


def max_sub_array_of_size_k(k, nums):
    """
    Max sum of any contiguous subarray of size ‘k’
    """
    max_sum = 0
    window_total, window_start = 0, 0
    for window_end in range(len(nums)):
        window_total += nums[window_end]
        if window_end >= (k - 1):
            max_sum = max(max_sum, window_total)
            window_total -= nums[window_start]
            window_start += 1
    return max_sum
