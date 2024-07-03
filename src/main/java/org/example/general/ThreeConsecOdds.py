from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        threeOdds = False
        for i in range(0, len(arr) - 2):
            if arr[i] % 2:
                if (arr[i + 1] % 2) and (arr[i + 2] % 2):
                    threeOdds = True
        return threeOdds

    # slower
    def threeConsecutiveOdds2(self, arr: List[int]) -> bool:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            if arr[i] % 2:
                dp[i] = 1 + dp[i + 1]
                if dp[i] == 3: return True
        return False
