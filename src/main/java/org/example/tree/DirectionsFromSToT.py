from typing import Optional, List

from org.example.tree.TreeNode import TreeNode


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # 1. Find LCA
        # 2. Find path from root to s
        # 3. Find path from root to t
        # 4. reverse path in LCA -> s as U and create final path

        lca_node = self.find_lca(root, startValue, destValue)

        path_to_start, path_to_dst = [], []
        directions = []

        self.find_path(lca_node, startValue, path_to_start)
        self.find_path(lca_node, destValue, path_to_dst)

        directions.extend("U" * len(path_to_start))
        directions.extend(path_to_dst)

        return "".join(directions)

    def find_lca(self, node: Optional[TreeNode], val1: int, val2: int) -> Optional[TreeNode]:
        if not node:
            return None

        if node.val == val1 or node.val == val2:
            return node

        left_lca = self.find_lca(node.left, val1, val2)
        right_lca = self.find_lca(node.right, val1, val2)

        if not left_lca:
            return right_lca
        elif not right_lca:
            return left_lca
        else:
            return node

    def find_path(self, node: Optional[TreeNode], targetVal: int, path: List[str]) -> bool:
        if not node:
            return False

        if node.val == targetVal:
            return True

        # Traverse left subtree first
        path.append("L")
        if self.find_path(node.left, targetVal, path):
            return True
        path.pop()

        path.append("R")
        if self.find_path(node.right, targetVal, path):
            return True
        path.pop()

        return False
