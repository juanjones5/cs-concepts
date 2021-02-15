class BinaryMatrix(object):
   def get(self, row: int, col: int) -> int:
       return 1
       
   def dimensions(self) -> list[]:
       return [4, 5]


def leftMostColumnWithOne(binaryMatrix: "BinaryMatrix") -> int:

    rows, cols = binaryMatrix.dimensions()

    def binary_search(row):
        nonlocal cols
        lo, hi = 0, cols - 1
        ans = float("inf")
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_val = binaryMatrix.get(row, mid)
            if mid_val == 0:
                lo = mid + 1
            else:
                ans = mid
                hi = mid - 1
        return ans

    solution = float("inf")
    for row in range(rows):
        solution = min(solution, binary_search(row))
    return -1 if solution == float("inf") else solution
