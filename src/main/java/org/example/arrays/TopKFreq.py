import heapq
from typing import List


class Solution(object):

    # T = O(n), M = (n), 56%
    # MaxHeap solution takes O(k logn) time,
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # 90%, T = O(k logn)
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        res, minH = [], []
        for key, val in freq.items():
            heapq.heappush(minH, (-val, key))
        while k > 0:
            k -= 1
            res.append(heapq.heappop(minH)[-1])
        return res
