from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(d, node):
            if not node or (not node.left and not node.right): return d
            leftDepth = rightDepth = 0
            if node.left:
                leftDepth = max(d, dfs(d + 1, node.left))
            if node.right:
                rightDepth = max(d, dfs(d + 1, node.right))
            return max(leftDepth, rightDepth)

        depth = dfs(1, root)
        return depth
