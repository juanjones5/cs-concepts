class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_BST(root: TreeNode, low: int, high: int) -> int:
    """
    Given the root node of a binary search tree, return the sum of
    values of all nodes with a value in the range [low, high].
    Time Complexity: O(N)
    Space: O(N)
    """

    def dfs(node):
        nonlocal ans
        if not node:
            return
        if node.val < low:
            dfs(node.right)
        elif node.val > high:
            dfs(node.left)
        else:
            ans += node.val
            dfs(node.left)
            dfs(node.right)

    ans = 0
    dfs(root)
    return ans


def convert_BST(root: TreeNode) -> TreeNode:
    """
    Given the root of a Binary Search Tree (BST), convert it to a
    Greater Tree such that every key of the original BST is changed
    to the original key plus sum of all keys greater than the original key in BST.
    """
    total = 0

    def dfs(node):
        nonlocal total
        if node is None:
            return None
        dfs(node.right)
        total += node.val
        node.val = total
        dfs(node.left)
        return node

    return dfs(root)


def tree_to_doubly_list(root: TreeNode) -> TreeNode:
    first = last = None

    def dfs(node):
        nonlocal first, last
        if not node:
            return
        dfs(node.left)
        if not first:
            first = node
        else:
            last.right = node
            node.left = last
        last = node
        dfs(node.right)

    dfs(root)
    if first:
        first.left, last.right = last, first
    return first