"""
CLONE GRAPH PROBLEM
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph
"""

from collections import defaultdict, deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph_recursive(node: Node) -> Node:
    visited = defaultdict(lambda: None)

    def dfs(current):
        if not current:
            return None
        if current.val in visited:
            return visited[current.val]
        clone = Node(current.val)
        visited[current.val] = clone
        for n in current.neighbors:
            clone.neighbors.append(dfs(n))
        return clone

    return dfs(node)


def clone_graph_iterative(node: Node) -> Node:
    if not node:
        return None
    helper_dict = {node: Node(node.val)}
    stack = [node]
    while stack:
        current = stack.pop()
        for n in current.neighbors:
            if n not in helper_dict:
                stack.append(n)
                helper_dict[n] = Node(n.val)
            helper_dict[current].neighbors.append(helper_dict[n])
    return helper_dict[node]


def clone_graph_bfs(node: Node) -> Node:
    if not node:
        return None
    visited = {node: Node(node.val)}
    queue = deque([node])
    while queue:
        current = queue.popleft()
        for n in current.neighbors:
            if n not in visited:
                queue.append(n)
                visited[n] = Node(n.val)
            visited[current].neighbors.append(visited[n])
    return visited[node]