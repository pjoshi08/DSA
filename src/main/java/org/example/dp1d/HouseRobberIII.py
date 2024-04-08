from typing import Optional

from org.example.tree.TreeNode import TreeNode


# https://leetcode.com/problems/house-robber-iii/description/
class Solution:
    """
    Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]

    """

    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0
            left = dfs(node.left)
            right = dfs(node.right)

            return node.val + left[1] + right[1], max(left) + max(right)

        return max(dfs(root))
