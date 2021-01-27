"""
BREADTH FIRST SEARCH
Tree BFS traversal.

- Time complexity: O(N) where N is the total number of Nodes
- Space: O(N) because we can have up to N/2 in the lowest level

Any problem involving the traversal of a tree in a level-by-level 
order can be efficiently solved using this approach

"""

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def level_by_level_traversal(root):
    """
    1. LEVEL-BY-LEVEL TRAVERSAL AS ARRAY
    Given a binary tree, populate an array to represent its
    level-by-level traversal. You should populate the values of all
    nodes of each level from left to right in separate sub-arrays.
    """
    result = []
    # 1. Add initial node to the queue
    queue = deque([root])
    while queue:
        # 2. Get Nodes to process at each level
        levels_at_node = len(queue)
        current_level_result = []
        # 3. Iterate through level nodes
        for _ in range(levels_at_node):
            # 4. Get current Node
            current = queue.popleft()
            # 5. Process current - PROBLEM LOGIC HERE
            current_level_result.append(current.val)
            # 6. Append children to the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        # 7. Add level result to main result
        result.append(current_level_result)
    return result


def min_depth(root) -> int:
    """
    2. MIN DEPTH
    Find the minimum depth of a binary tree. The minimum depth is the
    number of nodes along the shortest path from the root node to the
    nearest leaf node.
    """
    if not root:
        return 0
    # 1. Add initial node to the queue
    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        # 2. Get Nodes to process at each level
        nodes_at_level = len(queue)
        # 3. Iterate through level nodes
        for _ in range(nodes_at_level):
            # 4. Get current Node
            current = queue.popleft()
            # 5. Process current: check is current is leaf
            if not current.left and not current.right:
                return depth
            # 6. Append children to the queue
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return depth


def find_successor(root, key):
    """
    3. FIND SUCCESSOR
    Given a binary tree and a node, find the level order successor of the
    given node in the tree. The level order successor is the node that appears
    right after the given node in the level order traversal.
    """
    if not root:
        return None
    queue = deque([root])
    key_found = False
    while queue:
        nodes_at_level = len(queue)
        for _ in range(nodes_at_level):
            current = queue.popleft()
            if key_found:
                return current
            if current.val == key:
                key_found = True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return None


def right_view(root):
    """
    4. RIGHT VIEW OF TREE
    Given a binary tree, return an array containing nodes in its right view.
    The right view of a binary tree is the set of nodes visible when the tree
    is seen from the right side.
    """
    result = []
    queue = deque([root])
    while queue:
        nodes_at_level = len(queue)
        for i in range(nodes_at_level):
            current = queue.popleft()
            if i == nodes_at_level - 1:
                result.append(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    return result
