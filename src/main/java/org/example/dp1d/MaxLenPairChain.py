from typing import List

# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
class Solution:
    # DP Solution, T = O(n^2), M = O(n), slower
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    # Greedy Solution, T = O(nlogn), M = O(1)
    def findLongestChain2(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, length = float('-inf'), 0

        for p in pairs:
            if cur < p[0]:
                cur = p[1]
                length += 1
        return length


