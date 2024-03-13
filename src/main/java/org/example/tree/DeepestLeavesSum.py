from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Deepest Leaves Sum: https://leetcode.com/problems/deepest-leaves-sum/description/
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxLvl = 0
        total = 0

        def dfs(node, lvl):
            nonlocal maxLvl, total
            if not node: return
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

            if maxLvl < lvl:
                maxLvl = lvl
                total = 0
            if maxLvl == lvl:
                total += node.val

        dfs(root, 0)
        return total
