from heapq import heappop, heappush, nlargest

"""
MIN HEAP

Given an unsorted array of numbers, 
find the ‘K’ largest number in it


Time Complexity: O(N * log K)
Space: O(K)
"""


class Solution:
    def find_kth_largest(self, nums, k):
        k_min_heap = []
        # 1. Initialize a min heap with k elements
        for i in range(k):
            k_min_heap = heappush(k_min_heap, nums[i])
        # 2. Iterate through the array to make sure
        # we have the largest k elements in the min heap
        for j in range(k, len(nums)):
            if nums[j] > k_min_heap[0]:
                heappop(k_min_heap)
                heappush(k_min_heap, nums[j])
        # 3. From the largest k elements, return the smallest
        return k_min_heap[0]

    def find_kth_largest_easy(self, nums, k):
        return nlargest(k, nums)[-1]
