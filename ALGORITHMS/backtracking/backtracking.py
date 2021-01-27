"""
BACKTRACKING
Common Solution Structure
"""


class Backtracking:
    def __init__(self, n, g):
        self.n = n
        self.g = g
        self.solution = []

    def is_valid(self, v):
        return v in self.solution

    def backtrack(self):
        # GOAL - BASE CASE
        if len(self.solution) == self.n:
            return True
        for i in range(self.n):
            # CONSTRAINTS
            if self.is_valid(i):
                # Make a change if needed
                self.solution.append(i)
                # Recursive call + potential return
                worked = self.backtrack()
                if worked:
                    return True
                # Backtrack change
        return False


def backtracking(nums):
    solution = []

    def backtrack(index):
        # GOAL - BASE CASE
        if index == len(nums):
            return