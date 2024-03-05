from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(root, lvl):
            if root:
                q = [root]

                while q:
                    subList = []
                    for n in q:
                        subList.append(n.val)

                    if lvl % 2 != 0:
                        for n, val in zip(q, subList[::-1]):
                            n.val = val
                    qLen = len(q)
                    while qLen > 0:
                        node = q.pop(0)
                        if node.left: q.append(node.left)
                        if node.right: q.append(node.right)
                        qLen -= 1
                    lvl += 1
        reverse(root, 0)
        return root
