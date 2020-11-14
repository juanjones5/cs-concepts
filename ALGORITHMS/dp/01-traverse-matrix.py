'''
Write a program that counts how many ways you can go from the top-left to the bottom-right in a
2D array.
'''
class Solution:
    def solve(self, L):
        ways = -1 for i in range(len(L[0])) for j in range(len(L[0]))

'''
This is the given 2D Array
[
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]

We will store # of ways to get there
[
    [0, 1, 1, 1, 1],
    [1, 2, 3, 4, 5],
    [1, 3, 6, 10, 15],
    [1, 4, 10, 20, 35],
    [1, 5, 15, 35, 70]
]



For a given row, col; I got there from (row - 1, col) or (row, col - 1)

Recursively
(0,0) (0, 1)
(1, 0)

for i in range(n):
