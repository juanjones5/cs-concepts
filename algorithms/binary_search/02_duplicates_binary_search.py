def contains(arr, k):
    """
    CONTAINS
    Like a standard binary search
    """
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


def first(arr, k):
    """
    FIRST OCCURRENCE
    """
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


def last(arr, k):
    """
    LAST OCCURRENCE
    """
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


def ceiling(arr, k):
    """
    CEILING
    """
    lo, hi = 0, len(arr) - 1
    # Check if there's ceiling for k
    if k > arr[hi]:
        return -1
    while lo <= hi:
        mid = hi + (lo - hi) // 2
        if arr[mid] > k:
            hi = mid - 1
        elif arr[mid] < k:
            lo = mid + 1
        else:
            return mid
    return lo


def floor(arr, k):
    """
    FLOOR
    """
    lo, hi = 0, len(arr) - 1
    # Check if there's floor for k
    if k < arr[lo]:
        return -1
    while lo <= hi:
        mid = hi + (lo - hi) // 2
        if arr[mid] > k:
            hi = mid - 1
        elif arr[mid] < k:
            lo = mid + 1
        else:
            return mid
    return hi