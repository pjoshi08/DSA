import heapq
from typing import Optional

from org.example.tree.TreeNode import TreeNode

# Second Minimum Node In a Binary Tree:
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minH = []
        heapq.heapify(minH)

        def dfs(node):
            if not node: return

            if node.val not in minH:
                heapq.heappush(minH, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if len(minH) >= 2:
            heapq.heappop(minH)
        else:
            return -1
        return minH[0]
