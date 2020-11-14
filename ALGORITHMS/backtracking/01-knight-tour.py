"""
The knight is placed on the first block of an empty board and, moving 
according to the rules of chess, must visit each square exactly once.
"""
from pprint import pprint
TOTAL_POSSIBLE_MOVES = 8
# These two lists of moves are synced
X_POSSIBLE_MOVES = [2, 1, -1, -2, -2, -1, 1, 2]
Y_POSSIBLE_MOVES = [1, 2, 2, 1, -1, -2, -2, -1]

class KnightTour:

    def __init__(self, n):
        # Set size of the board
        self.n = n
        # Set all squares to non-visited, i.e. (-1)
        self.board = [[-1 for i in range(n)] for i in range(n)]

    # CONSTRAINTS
    def is_safe(self, x, y):
        return x >= 0 and y >= 0 and x < self.n and y < self.n and self.board[x][y] == -1

    def solve(self, move_count, x, y):
        # BASE CASE is we got to the end of the board
        if move_count == self.n ** 2:
            return True
        # For each square we have 8 possible moves around
        for i in range(TOTAL_POSSIBLE_MOVES):
            # we move to a new position
            new_x = x + X_POSSIBLE_MOVES[i]
            new_y = y + Y_POSSIBLE_MOVES[i]
            # we check if the landing position is valid, i.e. it is in the board
            if self.is_safe(new_x, new_y):
                # we set the square to the int of the step number
                self.board[new_x][new_y] = move_count
                # we solve recursively
                is_solution = self.solve(move_count + 1, new_x, new_y)
                if is_solution:
                    return True
                # if we get here is because something did not work, we set to -1
                self.board[new_x][new_y] = -1
        return False

    def print_result(self):
        pprint(self.board)

k = KnightTour(8)
if k.solve(0, 0, 0):
    k.print_result()