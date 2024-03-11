from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):  # returns a pair: [T/F, height of subtree]
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]