from collections import deque
from typing import List, Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    # T: O(n), M: O(n)
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)

        def dfs(node):
            if not node: return None

            # go to the lowest nodes first
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            # then check if a node needs to be deleted
            # if yes, save subtrees if they exist
            if node.val in to_delete:
                if node.left: res.append(node.left)
                if node.right: res.append(node.right)
                return None  # remove link from parent node

            return node

        root = dfs(root)
        if root:  # check if root was deleted or not
            res.append(root)
        return res

    # T: O(n), M: O(n), BFS solution, faster than dfs
    def delNodes2(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []
        q = deque([root])

        while q:
            node = q.popleft()
            # if left node exists, save it to queue and check if that node needs to be deleted
            if node.left:
                q.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
            # similarly check if right node exists, save it to queue and check if that node needs to be deleted
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete:
                    node.right = None

                    # check if current node needs to be deleted
            # if yes, save left and right subtrees if they exist
            if node.val in to_delete:
                if node.left: forest.append(node.left)
                if node.right: forest.append(node.right)

        # check if root node needs to be deleted
        if root.val not in to_delete:
            forest.append(root)
        return forest
