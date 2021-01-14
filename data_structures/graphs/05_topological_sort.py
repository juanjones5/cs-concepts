"""
Basic graph implementation in Python

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
from collections import defaultdict, deque
from pprint import pprint


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        # count of incoming edges of each vertex.
        # any vertex with ‘0’ in-degree will be a source
        self.in_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.in_degree[u]  # this will initialize it
        self.in_degree[v] += 1

    def topological_sort(self):
        sorted_order = []
        # 1. Find all sources, all vertices with 0 in-degrees
        # and add them to the queue
        sources = deque()
        for key in self.in_degree:
            if self.in_degree[key] == 0:
                sources.append(key)
        # 2. Process each source, add new ones as we process
        while sources:
            vertex = sources.popleft()
            sorted_order.append(vertex)
            for child in self.graph[vertex]:
                self.in_degree[child] -= 1
                if self.in_degree[child] == 0:
                    sources.append(child)
        # 3. Check the graph has no cycles
        if len(sorted_order) != len(self.in_degree):
            return []
        return sorted_order

    def print_graph(self):
        pprint(self.graph)
        pprint(self.in_degree)


# Driver code
g = Graph()
g.add_edge(3, 2)
g.add_edge(3, 0)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.print_graph()
