from typing import List
import heapq
from math import sqrt


def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    max_heap = []
    for point in points:
        b, h = point
        distance = sqrt(b ** 2 + h ** 2)
        if len(max_heap) < K:
            heapq.heappush(max_heap, (-distance, point))
        elif distance < -max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-distance, point))
    return [p for d, p in max_heap]