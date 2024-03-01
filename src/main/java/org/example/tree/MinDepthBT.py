from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Minimum Depth of Binary Tree: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + rightDepth  # right subtree exists
        if not root.right:
            return 1 + leftDepth  # left subtree exists
        return min(leftDepth, rightDepth) + 1
