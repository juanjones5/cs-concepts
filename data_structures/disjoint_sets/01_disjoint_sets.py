"""
DISJOINT SETS or UNION FIND DATA STRUCTURE
"""


class DisjointSetUnion(object):
    def __init__(self, size):
        # initially, each node is an independent component
        self.parent = [i for i in range(size + 1)]
        # keep the size of each component
        self.size = [1] * (size + 1)

    def find(self, x):
        """
        return the component id that the element x belongs to.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        merge the two components that x, y belongs to respectively,
        and return the merged component id as the result.
        """
        x_parent, y_parent = self.find(x), self.find(y)

        # the two nodes share the same set
        if x_parent == y_parent:
            return x_parent

        # otherwise, connect the two sets (components)
        if self.size[x_parent] > self.size[y_parent]:
            # add the node to the union with less members
            # keeping px as the index of the smaller component
            x_parent, y_parent = y_parent, x_parent
        # add the smaller component to the larger one
        self.parent[x_parent] = y_parent
        self.size[y_parent] += self.size[x_parent]
        # return the final (merged) group
        return y_parent