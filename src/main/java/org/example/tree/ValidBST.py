from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            if not node: return True
            if not (minVal < node.val < maxVal):
                return False
            return (dfs(node.left, minVal, node.val) and
                    dfs(node.right, node.val, maxVal))

        return dfs(root, float("-inf"), float("inf"))


n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2, n1, n3)
obj = Solution()
print(obj.isValidBST(n2))
