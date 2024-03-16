from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Path Sum: https://leetcode.com/problems/path-sum/description/
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        if not root.left and not root.right:
            return targetSum == root.val

        # leftSum = self.hasPathSum(root.left, targetSum - root.val)
        # rightSum = self.hasPathSum(root.right, targetSum - root.val)
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


obj = Solution()
n7 = TreeNode(7)
n2 = TreeNode(2)
n11 = TreeNode(11, n7, n2)
n4 = TreeNode(4, n11)
n1 = TreeNode(1)
n42 = TreeNode(4, right=n1)
n13 = TreeNode(13)
n8 = TreeNode(8, n13, n42)
n5 = TreeNode(5, n4, n8)
targetSum = 22
print(obj.hasPathSum(n5, targetSum))
