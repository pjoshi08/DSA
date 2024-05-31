class Solution(object):
    def minDistance(self, word1, word2):
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])
        return cache[0][0]

    # Caching, 77%
    def minDistance2(self, word1: str, word2: str) -> int:
        w1Len, w2Len = len(word1), len(word2)
        cache = {}  # (i, j): operations

        def dfs(i, j):
            if i == w1Len and j == w2Len: return 0
            if i == w1Len: return w2Len - j
            if j == w2Len: return w1Len - i
            if (i, j) in cache: return cache[(i, j)]

            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                insert = dfs(i, j + 1)
                delete = dfs(i + 1, j)
                replace = dfs(i + 1, j + 1)
                cache[(i, j)] = 1 + min(insert, delete, replace)
            return cache[(i, j)]
        return dfs(0, 0)
