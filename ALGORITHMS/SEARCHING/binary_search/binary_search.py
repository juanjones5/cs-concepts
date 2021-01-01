"""
ITERATIVE BINARY SEARCH
"""
def binary_search(arr, k):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

"""
RECURSIVE BINARY SEARCH
"""
def recursive_binary_search(arr, k, lo=0, hi=None):
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
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binary_search(arr, x) 
result2 = recursive_binary_search(arr, x) 
print(result)
print(result2)