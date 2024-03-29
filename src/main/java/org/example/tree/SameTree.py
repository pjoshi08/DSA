from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(p, q):
            if not p and not q: return True
            if (p and not q) or (not p and q): return False

            left = (p.val == q.val and dfs(p.left, q.left))
            right = (p.val == q.val and dfs(p.right, q.right))

            return left and right
        return dfs(p, q)