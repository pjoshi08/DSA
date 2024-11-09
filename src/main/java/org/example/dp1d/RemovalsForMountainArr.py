from typing import List


# 1671. Minimum Number of Removals to Make Mountain Array
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [1] * N  # longest increasing subsequence
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        LDS = [1] * N  # longest decreasing subsequence
        for i in reversed(range(N)):
            for j in range(i + 1, N):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], 1 + LDS[j])

        res = N
        for i in range(1, N - 1):  # 1 to N-1 for mountain constraint
            if min(LIS[i], LDS[i]) > 1:
                res = min(
                    res,
                    N - LIS[i] - LDS[i] + 1  # +1 as we count num twice in LIS and LDS
                )
        return res
