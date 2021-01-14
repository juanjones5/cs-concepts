from heapq import heappop, heappush, nsmallest

"""
MAX HEAP 

Given an unsorted array of numbers, 
find the ‘K’ smallest number in it

Time Complexity: O(N * log K)
Space: O(K)

Note: Python heapq is min heap
so we insert the negative values
to make it a max heap
"""


class Solution:
    def find_kth_smallest(self, nums, k):
        k_max_heap = []
        # 1. Initialize a MAX heap with k elements
        for i in range(k):
            k_max_heap = heappush(k_max_heap, -nums[i])
        # 2. Iterate through the array to make sure
        # we have the smallest k elements in the min heap
        for j in range(k, len(nums)):
            if nums[j] < -k_max_heap[0]:
                heappop(k_max_heap)
                heappush(k_max_heap, -nums[j])
        # 3. From the smallest k elements, return the largest
        return -k_max_heap[0]

    def find_kth_smallest_easy(self, nums, k):
        return nsmallest(k, nums)[-1]
