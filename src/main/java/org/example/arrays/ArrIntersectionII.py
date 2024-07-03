from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        freqB = {}
        for n in B:
            freqB[n] = 1 + freqB.get(n, 0)

        for n in A:
            if freqB.get(n, 0) > 0:
                res.append(n)
                freqB[n] -= 1
        return res
