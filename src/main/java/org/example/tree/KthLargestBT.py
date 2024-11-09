import heapq
from collections import deque
from typing import Optional

from org.example.tree.TreeNode import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        min_heap = []  # size will be at most k
        q = deque([root])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return -1 if len(min_heap) < k else min_heap[0]

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = []
        q = [root]

        while q:
            total = 0
            for _ in range(len(q)):
                node = q.pop(0)
                total += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            levels.append(-total)

        if len(levels) < k: return -1

        heapq.heapify(levels)
        while k > 0:
            kthLargest = heapq.heappop(levels)
            k -= 1
        return -kthLargest
