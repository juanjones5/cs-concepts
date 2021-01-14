"""
Given an array of numbers sorted in ascending order, 
find the element in the array that has the minimum 
difference with the given ‘key’
"""


def search_min_diff_element(arr, key):
    lo, hi = 0, len(arr) - 1
    if key < arr[lo]:
        return arr[lo]
    if key > arr[hi]:
        return arr[hi]
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > key:
            hi = mid - 1
        elif arr[mid] < key:
            lo = mid + 1
        else:
            return key
    # at this point, lo == hi + 1
    if (arr[lo] - key) < (arr[hi] - key):
        return arr[lo]
    return arr[hi]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()