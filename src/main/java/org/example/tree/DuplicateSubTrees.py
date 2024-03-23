import collections
from typing import Optional, List

from org.example.tree.TreeNode import TreeNode

#  Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/description/
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        count = collections.Counter()

        def encode(node):
            if not node: return ''

            # Need a left subtree and right subtree separator
            encoded = (str(node.val) + '#' + encode(node.left)
                       + '#' + encode(node.right))
            count[encoded] += 1
            if count[encoded] == 2:
                res.append(node)
            return encoded

        encode(root)
        return res
