from collections import deque
from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        q = deque([root])

        while q:
            cur_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level_sum.append(cur_sum)

        q = deque([(root, root.val)])  # (node, sibling_sum)
        level = 0
        while q:
            for _ in range(len(q)):
                node, sibling_sum = q.popleft()
                node.val = level_sum[level] - sibling_sum

                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                if node.right:
                    child_sum += node.right.val
                if node.left:
                    q.append((node.left, child_sum))
                if node.right:
                    q.append((node.right, child_sum))
            level += 1
        return root
