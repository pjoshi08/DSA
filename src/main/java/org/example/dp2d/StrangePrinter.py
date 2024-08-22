from collections import defaultdict


# video: https://www.youtube.com/watch?v=DSNGzJ63_Jg
class Solution:
    def strangePrinter(self, s: str) -> int:
        cache = defaultdict(int)

        def printer(i, j):
            if i > j: return 0
            if (i, j) in cache: return cache[(i, j)]

            res = 1 + printer(i + 1, j)  # try to print this letter
            for k in range(i + 1, j + 1):
                if s[i] == s[k]:
                    res = min(res, printer(i, k - 1) + printer(k + 1, j))
            cache[(i, j)] = res
            return res

        return printer(0, len(s) - 1)
