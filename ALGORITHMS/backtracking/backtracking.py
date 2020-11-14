class Backtracking:
    def __init__(self, n, g):
        self.n = n
        self.g = g
        self.solution = []

    def is_valid(self, v):
        return v in self.solution

    def solve(self):
        if (
            len(self.solution) == self.n 
            and self.solution[len(self.solution)] == 0
        ):
            return True
        for i in range(self.n):
            self.solution.append(i)
            worked = self.solve()
            if worked:
                return True

Solution().hola()