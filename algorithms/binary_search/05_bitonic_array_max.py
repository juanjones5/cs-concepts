"""
Find the maximum value in a given Bitonic array. 
An array is considered bitonic if it is monotonically 
increasing and then monotonically decreasing.
"""


def find_max_in_bitonic_array(arr):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > arr[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    # Since we use < in the while loop condition,
    # here lo == hi
    return arr[lo]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()