import heapq
import math
from collections import defaultdict
from typing import List


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
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
