"""
Basic tree implementation in Python
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Driver Code
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)


def invert_binary_tree(node: TreeNode) -> TreeNode:
    if not node:
        return None
    node.right, node.left = invert_binary_tree(node.left), invert_binary_tree(
        node.right
    )
    return node
