from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, isRoot, pathSum):
            if not node: return

            if isRoot:
                pathSum = node.val
            else:
                pathSum = pathSum * 10 + node.val

            if not node.left and not node.right:
                res.append(pathSum)
            else:
                dfs(node.left, False, pathSum)
                dfs(node.right, False, pathSum)

        dfs(root, True, 0)
        return sum(res)


obj = Solution()
n2 = TreeNode(2)
n3 = TreeNode(3)
n1 = TreeNode(1, n2, n3)
print(obj.sumNumbers(n1))
