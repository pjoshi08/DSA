from typing import Optional

from org.example.tree.TreeNode import TreeNode


# Flatten Binary Tree to LinkedList: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:  # we go the leftSubTree's rightmost node
                    prev = prev.right

                prev.right = curr.right  # we make the curr node's rightSubTree prev node's rightSubTree
                curr.right = curr.left  # we switch the leftSubTree to the right
                curr.left = None  # removing left
            curr = curr.right
