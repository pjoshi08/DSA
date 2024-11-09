# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
from typing import Optional, List

from org.example.tree.TreeNode import TreeNode


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        @cache
        def get_height(node):
            if not node: return 0

            return max(get_height(node.left), get_height(node.right)) + 1

        lookup = {}

        def calculate(node, depth, max_other):
            if not node: return

            left_height = get_height(node.left)
            right_height = get_height(node.right)

            if node.left:
                lookup[node.left.val] = max(right_height + depth, max_other)
                calculate(node.left, depth + 1, lookup[node.left.val])
            if node.right:
                lookup[node.right.val] = max(left_height + depth, max_other)
                calculate(node.right, depth + 1, lookup[node.right.val])

        calculate(root, 0, 0)
        ans = []
        for q in queries:
            ans.append(lookup[q])
        return ans
