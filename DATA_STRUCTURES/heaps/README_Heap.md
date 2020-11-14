
## DATA STRUCTURE: Heap / Priority Queue
A heap is a specialized complete binary tree.

**Heap property** the key at each node is at least as great as the keys stored
at its children.

- max-heap
- min-heap

Implemented as an array. The children of a node at index i ar at 2i+1 and 2i+2

Time:
- Insert `O(log n)`
- Lookup max or min `O(1)`
- Deletion of max or min `O(log n)`
- Searching for arbitrary keys takes `O(n)`

Python:
- Library: `heapq` - MIN HEAP ONLY, if you need max-heap, insert their negatives.
- `heapq.heapify(L)` make L a heap in place.
- `heapq.nlargest(k, L)` or `heapq.nsmallest(k, L)`
- `heapq.heappush(L, e)`
- `heapq.heappop(L)` smallest element from the heap