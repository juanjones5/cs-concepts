import math

"""
Given an infinite sorted array (or an array with unknown size), 
find if a given number ‘key’ is present in the array. Write a 
function to return the index of the ‘key’ if it is present in 
the array, otherwise return -1.

Time Complexity: O(log N)
Space: O(1)
"""


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # 1. Find the bounds
    lo, hi = 0, 1
    while key > reader.get(hi):
        diff = hi - lo
        lo = hi + 1
        hi = lo + diff * 2
    # 2. Apply regular binary search
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if key > reader.get(mid):
            lo = mid + 1
        elif key < reader.get(mid):
            hi = mid - 1
        else:
            return mid
    return -1


def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()