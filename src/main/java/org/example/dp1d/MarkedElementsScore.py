import heapq
from typing import List


# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score, size = 0, len(nums)
        minh = [(nums[i], i) for i in range(size)]  # stores (n, index) in heap
        marked = {}
        heapq.heapify(minh)
        for i in range(size):
            minV, idx = heapq.heappop(minh)
            if idx not in marked:
                score += minV
                marked[idx] = marked[idx - 1] \
                    = marked[idx + 1] = 1
        return score
