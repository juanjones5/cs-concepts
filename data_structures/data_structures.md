## 1. ARRAY

## 2. LINKED LIST

## 3. STACK

## 4. QUEUE

## 5. HEAP

## 6. TREE

===================================================================

## 7. TRIE
Useful for dealing with string prefixes.
Implement:
1. Build Node class with `self.children = [None] * 26`, `is_end` boolean
2. Build Trie class with `self.root = Node()`
3. Implement `insert`
4. Implement `search`

===================================================================

## 8. BST
Search: O(log N)
Insert: O(log N)
Delete: O(log N)
Hash tables do these operations faster, so only use a BST if we
need to get all the keys in sorted order, or we need to do range
operations (since similar value elements are close)

Implement:
1. Build Node class with `value`, `left` and `right`

===================================================================

## 9. HASH TABLE / HASH MAP
Store any info that needs to be searched by an index in O(1)
Insert and Delete are also O(1)

===================================================================

## 10. GRAPH
To represent elements that share connections.

Implement:
1. Build the dictionary `graph = defaultdict(list)`
2. Add all the edges


Applications:

- DFS
  `visited = defaultdict(lambda: False)` and `while stack`

- BFS
  `visited = defaultdict(lambda: False)` and `while queue`

- Topological Sort: 
  For directed acyclic graphs (DAG)
  Used for scheduling jobs
  to find a linear ordering of elements that have dependencies on each other
  `graph = defaultdict(list)`
  `in_degree = defaultdict(int)`
  we do a `while queue` with the vertices that have 0 `in_degree`
  `len(topological_sort) == len(in_degree)`

===================================================================

## 11. DISJOINT SETS
To keep track of the connected components of an undirected graph.
Two main applications:
- Two vertices belong to the same connected component?
- Adding an edge would result in a cycle?

Implement:
1. Create a class with `parent` and `size` arrays
2. Implement `find` recursively and `union` methods
