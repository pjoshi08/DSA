from typing import List, Optional

from org.example.tree.TreeNode import TreeNode


# Binary Tree Zigzag Level Order Traversal:
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [root]
        res = []
        reverse = False
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                if reverse:
                    res.append(level[::-1])
                else:
                    res.append(level)
                reverse = not reverse
        return res


obj = Solution()
n15 = TreeNode(15)
n7 = TreeNode(7)
n20 = TreeNode(20, n15, n7)
n9 = TreeNode(9)
root = TreeNode(3, n9, n20)
print(obj.zigzagLevelOrder(root))
