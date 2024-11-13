from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            for n in candidates:
                # inc cnt if bit is set at the ith bit of n
                # left shift 1 by i and & it with n to see if bit is set
                cnt += 1 if (1 << i) & n else 0
            res = max(res, cnt)
        return res
