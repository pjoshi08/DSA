from typing import List


# https://leetcode.com/problems/extra-characters-in-a-string/description/
# Check TrieNode solution (faster)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)

        for i in reversed(range(len(s))):
            dp[i] = 1 + dp[i + 1]
            for w in dictionary:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = min(dp[i], dp[i + len(w)])

        return dp[0]


obj = Solution()
s = "leetscode"
dictionary = ["leet", "code", "leetcode"]
print(obj.minExtraChar(s, dictionary))
