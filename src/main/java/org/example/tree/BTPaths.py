from typing import List, Optional

from org.example.tree.TreeNode import TreeNode

# https://leetcode.com/problems/binary-tree-paths/description/
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def dfs(node, path):
            if not node: return

            path += str(node.val)
            if not node.left and not node.right:
                res.append(path)
            else:
                dfs(node.left, path + '->')
                dfs(node.right, path + '->')

        dfs(root, '')
        return res
