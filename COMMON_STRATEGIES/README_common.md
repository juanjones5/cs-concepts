## TWO POINTERS
- Sorted arrays, example `two_sum_ii`

1. SLIDING WINDOW
The input is an array or a linked list. We are asked to find or 
calculate something among all the contiguous subarrays (or sublists) 
of a given size.   

2. TWO POINTERS
The input is a sorted array or linked list and we need to find a 
set of elements (pair, triplet, subarray) that fulfill certain constraints.

1. FAST & SLOW POINTERS
For dealing with cyclic LinkedLists or arrays.

2. MERGE INTERVALS
The input is usually an array of intervals represented as arrays as well.
The problem is usually related to finding overlapping.
The first step is to sort the intervals by start time. This usually gives
us the running time of O(N log N), unless the intervales were sorted before.
Space complexity tends to be O(N) which is required for sorting. 

5. CYCLIC SORT
The input is an array containing numbers in a given range, 0 to N or 1 to N
We need to find the duplicate, missing number, etc.
We can do a cyclic sort, basically swapping numbers as we iterate the array

6. IN-PLACE REVERSAL OF LINKED LIST
We need to do this in-place, i.e., using the existing node objects 
and without using extra memory.

7. TREE BFS
When we are asked to process level by level

8. TREE DFS
When the problem is related to paths from root to leaf

9.  TWO HEAPS
This pattern uses two Heaps to solve these problems; A Min Heap to find the smallest element and a Max Heap to find the biggest element

10. SUBSETS
11. MODIFIED BINARY SEARCH
12. BITWISE XOR
13. TOP K ELEMENTS
14. K-WAY MERGE
15. DP: 0/1 KNAPSACK
16. GRAPH TOPOLOGICAL SORT