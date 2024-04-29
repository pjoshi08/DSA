# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


# https://leetcode.com/problems/clone-n-ary-tree/
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for child in node.children:
                copy.children.append(dfs(child))
            return copy

        return dfs(root)
