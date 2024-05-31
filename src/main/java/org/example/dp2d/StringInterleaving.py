class Solution(object):
    # 22%
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        return dp[0][0]

    # caching is faster, 58%
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        s1Len, s2Len, s3Len = len(s1), len(s2), len(s3)
        if s1Len + s2Len != s3Len: return False

        dp = {}  # (i, j): True/False, where i, j are indices for s1, s2

        def dfs(i, j):  # k = i + j
            if i == s1Len and j == s2Len: return True
            if (i, j) in dp: return dp[(i, j)]

            # no need to cache if we find it true even one, we just return
            if i < s1Len and s3[i + j] == s1[i] and dfs(i + 1, j):
                return True
            if j < s2Len and s3[i + j] == s2[j] and dfs(i, j + 1):
                return True
            dp[(i, j)] = False
            return False
        return dfs(0, 0)