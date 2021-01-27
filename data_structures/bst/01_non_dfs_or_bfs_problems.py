class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def closest_value(root: TreeNode, target: float) -> int:
    """
    Given a non-empty binary search tree and a target value,
    find the value in the BST that is closest to the target.
    Time Complexity: O(H) it would be O(log N) if the bst is balanced
    Space: O(1)
    """
    r = root.val
    while root:
        if abs(root.val - target) < abs(r - target):
            r = root.val
        root = root.left if target < root.val else root.right
    return r