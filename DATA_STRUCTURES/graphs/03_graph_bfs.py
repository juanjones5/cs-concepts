"""
Simple Connected Graph BFS traversal.
Same as tree but add "visited" data structure
to check for cycles.
- Time complexity: O(V+E)
- Space: O(V)

Applications:
1. Shortest Path and MST, for weighted graphs
2. P2P Network, use BFS to find neighbor nodes.
3. Crawlers, better than DFS because we can limit depth.
4. Social Network, find people within 'k' level distance (depth)
5. GPS, find neighboring locations.

"""
from collections import defaultdict, deque

class GraphBFS:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, u):
        # 1. Add the initial vertex to the queue
        queue = deque([u])
        # 2. Initialize visited data structure
        visited = defaultdict(lambda: False)
        while queue:
            # 3. Dequeue element 
            current = queue.popleft()
            print(current, end='')
            # 4. Mark element as visited
            visited[current] = True
            # 5. Add all children to the stack if not visited yet
            for v in self.graph[current]:
                if not visited[v]:
                    queue.append(v)

# Driver program
g = GraphBFS() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
g.bfs(2)
print()