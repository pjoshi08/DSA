# Definition for Node.
from typing import Optional

# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/description/
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


NodeCopy = type('NodeCopy', Node.__bases__, dict(Node.__dict__))


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        oldToNew = {}  # {Node: NodeCopy}

        def dfs(node):
            if not node: return None
            if node in oldToNew: return oldToNew[node]

            copy = NodeCopy(node.val)
            oldToNew[node] = copy
            copy.left = dfs(node.left)
            copy.right = dfs(node.right)
            copy.random = dfs(node.random)

            return copy

        return dfs(root)
