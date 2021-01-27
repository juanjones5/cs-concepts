"""
Basic graph implementation in Python
"""
from collections import defaultdict
from pprint import pprint


class Graph:
    def __init__(self):
        # The defaultdict can be defaulted to list or set
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        # self.graph[v].append(u) # for undirected graphs

    def print_graph(self):
        pprint(self.graph)


# Driver code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.print_graph()