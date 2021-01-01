Graphs are ideal for modeling and analyzing relationships between pairs of objects. 

**It’s natural to use a graph when the problem involves spatially connected objects, e.g., road
segments between cities.
More generally, consider using a graph when you need to analyze any binary relationship,
between objects, such as interlinked webpages, followers in a social graph, etc. In such cases,
quite often the problem can be reduced to a well-known graph problem.
Some graph problems entail analyzing structure, e.g., looking for cycles or connected components. DFS works particularly well for these applications.
Some graph problems are related to optimization, e.g., find the shortest path from one vertex to
another. BFS, Dijkstra’s shortest path algorithm, and minimum spanning tree are examples
of graph algorithms appropriate for optimization problems.**


Graph Search:
DFS and BFS differ from each other in terms of the additional information they provide, e.g.,
BFS can be used to compute distances from the start vertex and DFS can be used to check for the
presence of cycles. Key notions in DFS include the concept of discovery time and finishing time for
vertices.

## DAG
A directed acyclic graph (DAG) is a directed graph in which there are no cycles, i.e., paths which
contain one or more edges and which begin and end at the same vertex.

A topological ordering of the vertices in a DAG is an ordering of the vertices in which each
edge is from a vertex earlier in the ordering to a vertex later in the ordering.

If G is an undirected graph, vertices u and v are said to be connected if G contains a path from
u to v; otherwise, u and v are said to be disconnected.

Graphs naturally arise when modeling geometric problems, such as determining connected
cities. 

A graph can be implemented in two ways—using adjacency lists or an adjacency matrix.

 In the
adjacency list representation, each vertex v, has a list of vertices to which it has an edge. The
adjacency matrix representation uses a |V| × |V| Boolean-valued matrix indexed by vertices, with
a 1 indicating the presence of an edge. The time and space complexities of a graph algorithm are
usually expressed as a function of the number of vertices and edges.