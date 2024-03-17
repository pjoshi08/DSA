from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
class Solution:
    # Better than solution 2, O(n) = 26ms(97%), O(1) memory
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, pathSum):
            if not node: return 0

            pathSum = pathSum * 10 + node.val
            if not node.left and not node.right:
                return pathSum
            return dfs(node.left, pathSum) + dfs(node.right, pathSum)

        return dfs(root, 0)

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, isRoot, pathSum):
            if not node: return

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
