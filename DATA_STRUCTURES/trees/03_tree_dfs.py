"""
DEPTH FIRST SEARCH
Tree DFS traversal.

- Time complexity: O(N) where N is the total number of Nodes
- Space: O(H) where H is the height of the tree

Any search for a root-to-leaf path

Using recursion, we can create a recursive closure
adding parameters that will serve as state.
"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def has_path(root, total):
    """
    1. BINARY TREE PATH SUM - Boolean
    Given a binary tree and a number 'total', find if the tree
    has a path from root-to-leaf such that the sum of all
    the node values of that path equals ‘total’
    """

    # Base Case 1
    if not root:
        return False
    # Base Case 2: node is leaf and matches total
    if not root.left and not root.right and root.val == total:
        return True
    # DFS to the left and DFS to the right
    return has_path(root.left, total - root.val) or has_path(
        root.right, total - root.val
    )


def find_paths(root, total):
    """
    2. BINARY TREE PATH SUM - Actual Paths
    Given a binary tree and a number ‘total’, find all paths
    from root-to-leaf such that the sum of all the node
    values of each path equals ‘total’
    """
    all_paths = []

    def find_paths_recursive(current, required_sum, current_path):
        if current is None:
            return

        # add the current node to the path
        current_path.append(current.val)

        # if the current node is a leaf and its value is equal to required_sum, save the current path
        if (
            current.val == required_sum
            and current.left is None
            and current.right is None
        ):
            all_paths.append(list(current_path))
        else:
            # traverse the left sub-tree
            find_paths_recursive(current.left, required_sum - current.val, current_path)
            # traverse the right sub-tree
            find_paths_recursive(
                current.right, required_sum - current.val, current_path
            )

        # remove the current node from the path to backtrack,
        # we need to remove the current node while we are going up the recursive call stack.
        del current_path[-1]

    find_paths_recursive(root, total, [])
    return all_paths


def path_with_sequence(root, sequence) -> bool:
    """
    3. PATH WITH SEQUENCE
    Given a binary tree and a number sequence,
    find if the sequence is present as a
    root-to-leaf path in the given tree
    """

    def dfs(node, path):
        if not node:
            return False
        path.append(node.val)
        if not node.left and not node.right and path == sequence:
            return True
        return dfs(node)