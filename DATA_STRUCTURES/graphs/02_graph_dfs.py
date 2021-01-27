"""
Simple Graph DFS traversal.
Same as tree but add "visited" data structure
to check for cycles.
- Time complexity: O(V+E)
- Space: O(V)

Applications:
1. Find MST, for weighted graphs
2. Detect Cycles: do DFS and return True if there is a back edge
3. Path Finding, call DFS with origin and return the stack when the 
detination is found.
4. Topological Sorting, for shceduling jobs
5. Graph is Bipartite test
6. Finding Strongly Connected Components, path from each vertex in 
the graph to every other vertex.
7. Solving puzzles with only one solution, such as mazes.
"""
from collections import defaultdict, deque


class GraphDFS:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_iterative(self, u):
        # 1. Add the initial vertex to the stack
        stack = [u]
        # 2. Initialize visited data structure
        visited = defaultdict(lambda: False)
        while len(stack):
            # 3. Pop and process last element of the stack
            current = stack.pop()
            print(current, end="")
            # 4. Mark element as visited
            visited[current] = True
            # 5. Add all children to the stack if not visited yet
            for v in self.graph[current]:
                if not visited[v]:
                    stack.append(v)

    def dfs_recursive(self, u, visited=defaultdict(lambda: False)):
        print(u, end="")
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.dfs_recursive(v, visited)

    def dfs_disconnected_graph(self):
        # We run DFS for each vertext
        visited = defaultdict(lambda: False)
        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs_recursive(vertex, visited)


# Driver program to test methods of graph class

g = GraphDFS()
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(1, 4)

print("Iterative DFS")
g.dfs_iterative(0)
print()
print("Recursive DFS")
g.dfs_recursive(0)
print()