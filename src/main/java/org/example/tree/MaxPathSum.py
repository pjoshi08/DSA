from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # Compute sum without the split
        def dfs(node):
            if not node: return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            # compute sum WITH the split
            res[0] = max(res[0], node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
