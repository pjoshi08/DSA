from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: break
        return dp[0]

    # 90%
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        strLen = len(s)
        dp = [False] * (strLen + 1)
        dp[strLen] = True
        for i in reversed(range(strLen)):
            for w in wordDict:
                wordLen = len(w)
                if (i + wordLen <= strLen) and s[i: i + wordLen] == w:
                    dp[i] = dp[i + wordLen]
                    if dp[i]: break
        return dp[0]
