from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def dfs(node):
            nonlocal ans
            if not node:
                ans += "None,"
                return
            ans += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)

        ans = ""
        dfs(root)
        return ans

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def dfs(queue):
            if queue[0] == "None":
                queue.popleft()
                return None
            node = TreeNode(queue.popleft())
            node.left = dfs(queue)
            node.right = dfs(queue)
            return node

        return dfs(deque(data.split(",")))