from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left + right)  # diameter from a particular node

            return 1 + max(left, right)  # tree height

        dfs(root)
        return res[0]
