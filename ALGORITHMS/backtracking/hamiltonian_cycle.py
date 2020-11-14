"""
Hamiltonian Path in an undirected graph is a path that visits each 
vertex exactly once. A Hamiltonian cycle is a Hamiltonian Path such 
that there is an edge (in the graph) from the last vertex to the 
first vertex of the Hamiltonian Path. 
Determine whether a given graph contains Hamiltonian Cycle or not. 
If it contains, then prints the path. 
"""

class Hamiltonian:
    def __init__(self, n, g):
        self.n = n
        self.g = g
        self.solution = []

    def is_valid(self, v):
        return v in self.solution

    def solve(self):
        if (
            len(self.solution) == self.n 
            and self.solution[len(self.sol)] == 0
        ):
            return True
        for i in range(self.n):
            self.solution.append(i)
            worked = self.solve()
            if worked:
                return True

Solution().hola()