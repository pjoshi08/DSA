from collections import defaultdict


# https://leetcode.com/problems/decode-ways-ii/
class Solution:
    def numDecodings(self, s: str) -> int:
        count = defaultdict(int)
        for i in range(1, 27): count[str(i)] = 1
        for i in range(10): count["*" + str(i)] = 1 + (i < 7)  # count for 11-26
        # *: 1-9, **: 11-26, 1*: 11-19, 2*: 21-26
        count["*"], count["**"], count["1*"], count["2*"] = 9, 15, 9, 6

        n, mod = len(s) - 1, 10 ** 9 + 7
        dp = [count[s[0]]] + [0] * n + [1]

        for i in range(n):
            one, two = s[i + 1], s[i] + s[i + 1]

            dp[i + 1] = (count[one] * dp[i] + count[two] * dp[i - 1]) % mod
            if not dp[i + 1]: return 0
        return dp[-2]


obj = Solution()
# s = "*"
# s = "1*"
s = "094"
print(obj.numDecodings(s))
