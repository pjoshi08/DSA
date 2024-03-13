import collections
from typing import List, Optional

from org.example.tree.TreeNode import TreeNode


# Binary Tree Inorder Traversal
class Solution:
    # Iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:  # because of stack, we reverse the order, right -> root -> left
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

    # Recursive
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []

        def dfs(node):
            if not node: return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res


n3 = TreeNode(3)
n2 = TreeNode(2, n3)
n1 = TreeNode(1, right=n2)
obj = Solution()
print(obj.inorderTraversal(n1))
