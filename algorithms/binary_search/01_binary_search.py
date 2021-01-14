"""
BINARY SEARCH

For sorted arrays

Time Complexity: O(log N)
Space: O(1)

Note about ending status: 
- (while lo <= hi) => lo == hi+1
- (while lo < hi) => lo == hi
"""


def binary_search(arr, k):
    """
    ITERATIVE BINARY SEARCH
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > k:
            hi = mid - 1
        elif arr[mid] < k:
            lo = mid + 1
        else:
            return mid
    return -1


def recursive_binary_search(arr, k, lo=0, hi=None):
    """
    RECURSIVE BINARY SEARCH
    """
    if not hi:
        hi = len(arr) - 1
    if hi >= lo:
        mid = lo + (hi - lo) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return recursive_binary_search(arr, k, lo, mid - 1)
        else:
            return recursive_binary_search(arr, k, mid + 1, hi)
    else:
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, x)
result2 = recursive_binary_search(arr, x)
print(result)
print(result2)