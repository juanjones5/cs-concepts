"""
Basic graph implementation in Python

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
from collections import defaultdict, deque
from pprint import pprint
from typing import List


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


def can_finish_course_schedule(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    COURSE SCHEDULE PROBLEM
    There are a total of numCourses courses you have to take,
    labeled from 0 to numCourses-1.
    Some courses may have prerequisites, for example to take course 0
    you have to first take course 1, which is expressed as a pair: [0,1]
    Given the total number of courses and a list of prerequisite pairs,
    is it possible for you to finish all courses?
    """
    if not prerequisites:
        return True
    graph = defaultdict(list)
    in_degree = {num: 0 for num in range(numCourses)}
    topological_sort = []
    # Build Graph
    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        in_degree[pre[0]] += 1
    # Find starting vertices
    queue = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            queue.append(key)
    # Build topological sort
    while queue:
        current = queue.popleft()
        topological_sort.append(current)
        for v in graph[current]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    # Return False if the sort has a cycle
    return len(topological_sort) == len(in_degree)
