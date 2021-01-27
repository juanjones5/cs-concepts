"""
Dijkstra Algorithm
Find shortest paths from source to all vertices in the graph
"""
from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)  

    