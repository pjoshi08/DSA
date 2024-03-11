import collections
from typing import List, Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = [root]
        res = [root.val]
        while q:
            qLen = len(q)
            for _ in range(qLen):
                node = q.pop(0)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if q: res.append(q[-1].val)
        return res

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: res.append(rightSide.val)
        return res
   