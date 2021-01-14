from heapq import heappush, heappop
from collections import defaultdict, Counter
from typing import List


def top_k_most_frequent(nums, k):
    """
    MIN HEAP
    Given an unsorted array of numbers,
    find the top ‘K’ frequently occurring numbers in it

    Time Complexity: O(N * log K)
    Space: O(N)

    Note: When we need to compare objects with heapq
    we can use tuples (it uses the first value) or we can
    implement __cmp__ or __lt__ in the class
    """
    # 1. Create a dictionary with frequencies
    frequencies = defaultdict(int)
    for num in nums:
        frequencies[num] += 1
    # 2. Initialize the min heap
    k_min_heap = []
    for i in range(k):
        heappush(k_min_heap, (frequencies[nums[i]], nums[i]))
    for j in range(k, len(frequencies)):
        if frequencies[nums[j]] > k_min_heap[0][0]:
            heappop(k_min_heap)
            heappush(k_min_heap, (frequencies[nums[j]], nums[j]))
    return [x[1] for x in k_min_heap]


class Character:
    def __init__(self, count, value):
        self.count = count
        self.value = value

    def __lt__(self, other):
        return (
            self.value > other.value
            if self.count == other.count
            else self.count < other.count
        )

    def __eq__(self, other):
        return self.count == other.count and self.value == other.value


def topKFrequent(self, words: List[str], k: int) -> List[str]:
    """
    Given a non-empty list of words, return the k most frequent elements.
    Your answer should be sorted by frequency from highest to lowest.
    If two words have the same frequency, then the word with the lower
    alphabetical order comes first.

    Time Complexity: O(N * log K)
    Space: O(N)
    """
    c = Counter(words)
    min_heap = []
    for key, val in c.items():
        current = Character(val, key)
        if len(min_heap) < k:
            heappush(min_heap, current)
        else:
            if current > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, current)
    return [x.value for x in sorted(min_heap)[::-1]]