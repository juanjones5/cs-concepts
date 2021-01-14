from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    """
    MAXIMAL SQUARE
    Given an m x n binary matrix filled with 0's and 1's,
    find the largest square containing only 1's and
    return its area.
    Time Complexity: O(m n)
    Space: O(1)"""
    max_squares = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = int(matrix[row][col])
            if matrix[row][col] == 1 and row > 0 and col > 0:
                matrix[row][col] = (
                    min(
                        matrix[row][col - 1],
                        matrix[row - 1][col - 1],
                        matrix[row - 1][col],
                    )
                    + 1
                )
            max_squares = max(max_squares, matrix[row][col])
    return max_squares * max_squares


def maximal_rectangle(matrix: List[List[str]]) -> int:
    """
    MAXIMAL RECTANGLE
    Given an m x n binary matrix filled with 0's and 1's,
    find the largest rectangle containing only 1's and
    return its area.
    Time Complexity: O(m^2 n)
    Space: O(1)
    """
    max_area = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] = int(matrix[row][col])
            if matrix[row][col] == 0:
                continue

            width = matrix[row][col] = matrix[row][col - 1] + 1 if col else 1

            # compute the maximum area rectangle with a lower right corner at [row, col]
            k = row
            while k > -1:
                # width will always be the min of the positive values
                # above the current cell
                width = min(width, matrix[k][col])
                max_area = max(max_area, width * (row - k + 1))
                k -= 1
    return max_area