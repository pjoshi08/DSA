import heapq
from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    # Better than minH solution and Neetcode's solution
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n, stack = 0, [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    n += 1
                    if n == k: return node.val
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

    # Neetcode's solution
    def kthSmallest0(self, root: Optional[TreeNode], k: int) -> int:
        n, stack, cur = 0, [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k: return cur.val
            cur = cur.right

    # MinHeap solution
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        def dfs(node):
            if not node: return

            heapq.heappush(heap, node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        if k == 1: return heap[0]
        for i in range(k - 1):
            heapq.heappop(heap)
        return heap[0]
