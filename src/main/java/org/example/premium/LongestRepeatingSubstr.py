# Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0.
#
#
#
# Example 1:
#
# Input: s = "abcd"
# Output: 0
# Explanation: There is no repeating substring.
# Example 2:
#
# Input: s = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
# Example 3:
#
# Input: s = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.
class Solution:
    # dp solution
    # create O(n^2) substr and match each character, inc count based on prev matched chars
    # T: O(n^2), M: O(n^2)
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        res = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # match each char
                # update count based on the previously matched char
                if s[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res