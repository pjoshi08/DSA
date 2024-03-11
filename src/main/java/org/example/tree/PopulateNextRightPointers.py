from typing import Optional


# Populating Next Right Pointers in Each Node:
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        q = [root]
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.pop(0)
                if i == qLen - 1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return root

