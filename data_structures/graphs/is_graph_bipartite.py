"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into 
two independent subsets A and B, such that every edge in the graph has 
one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes 
j for which the edge between nodes i and j exists.  Each node is an 
integer between 0 and graph.length - 1.  There are no self edges or 
parallel edges: graph[i] does not contain i, and it doesn't contain 
any element twice.

Time Complexity: O(N + E) N is number of nodes in the graph, E = edges
Space Complexity: O(N)
"""

from typing import List
from collections import deque, defaultdict


def is_bipartite_bfs(graph: List[List[int]]) -> bool:
    data = defaultdict(lambda: None)
    for node in range(len(graph)):
        if not data[node]:
            queue = deque([(node, "A")])
            while queue:
                current = queue.popleft()
                data[current[0]] = current[1]
                neighbor_set = "A" if current[1] == "B" else "B"
                for v in graph[current[0]]:
                    if data[v] == current[1]:
                        return False
                    if not data[v]:
                        queue.append((v, neighbor_set))
    return True