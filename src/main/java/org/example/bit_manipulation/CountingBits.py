class Solution:

    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

    def countBits2(self, n: int) -> list[int]:
        res = [0]

        for i in range(1, n + 1):
            count = 0
            while i:
                i &= (i - 1)
                count += 1
            res.append(count)
        return res


obj = Solution()
print(obj.countBits(5))
