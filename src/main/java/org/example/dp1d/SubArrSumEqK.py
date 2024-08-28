from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # because we are computing prefixSum - k, for base case
        # when we reach k, increment by 1
        dp = {0: 1}
        prefixSum, count = 0, 0

        for n in nums:
            prefixSum += n
            if prefixSum - k in dp:
                count += dp[prefixSum - k]
            dp[prefixSum] = 1 + dp.get(prefixSum, 0)
        return count
