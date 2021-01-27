"""
Given the root of a Binary Search Tree (BST), convert it to a 
Greater Tree such that every key of the original BST is changed 
to the original key plus sum of all keys greater than the original key in BST.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        self.convertBST(root.right)
        self.total += root.val
        root.val = self.total
        self.convertBST(root.left)
        return root