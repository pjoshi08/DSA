import collections
from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
class Codec:

    # Leetcode: 97%
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        res = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        data = collections.deque(data.split(","))
        root = TreeNode(int(data.popleft()))
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if (left := data.popleft()) != "N":
                node.left = TreeNode(int(left))
                q.append(node.left)
            if (right := data.popleft()) != "N":
                node.right = TreeNode(int(right))
                q.append(node.right)
        return root

    # Below solution works, 45% on leetcode
    def serialize2(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize2(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
