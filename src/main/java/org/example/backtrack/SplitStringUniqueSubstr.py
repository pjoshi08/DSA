class Solution:
    # M: O(n * n * 2^n), n to slice s, n for inner loop, 2^n for backtracking
    def maxUniqueSplit(self, s: str) -> int:
        sLen = len(s)

        def dfs(i, cur_set):
            if i == sLen:
                return 0

            res = 0
            for j in range(i, sLen):
                subStr = s[i:j + 1]
                if subStr in cur_set:
                    continue
                cur_set.add(subStr)
                res = max(res, 1 + dfs(j + 1, cur_set))
                cur_set.remove(subStr)

            return res

        return dfs(0, set())
