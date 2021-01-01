"""
CONTAINS
Like a standard binary search
"""
def contains(arr, k):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < k:
            lo = mid + 1
        elif arr[mid] > k:
            hi = mid - 1
        else:
            return True
    return False

"""
FIRST OCCURRENCE
"""
def first(arr, k):
    lo, hi = 0, len(arr) - 1
    ans = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > k:
            hi = mid - 1
        elif arr[mid] < k:
            lo = mid + 1
        else:
            ans = mid
            hi = mid - 1
    return ans

"""
LAST OCCURRENCE
"""
def last(arr, k):
    lo, hi = 0, len(arr) - 1
    ans = -1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > k:
            hi = mid - 1
        elif arr[mid] < k:
            lo = mid + 1
        else:   
            ans = mid
            lo = mid + 1
    return ans
    

