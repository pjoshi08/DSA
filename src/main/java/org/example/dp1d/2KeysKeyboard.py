class Solution:
    # DP solution
    # T: O(n^2), M: O(n)
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        dp[1] = 0  # step to reach 1 A

        for i in range(2, n + 1):
            # we only need to compute till n / 2
            # because pasting from n/2 will make us reach n
            # also we add 1 because we want to include i // 2th value
            for j in range(1, 1 + (i // 2)):
                if i % j == 0:  # if j is a factor of i
                    # add how many times we had to use j to reach i
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]

    # recursion with cache
    # T: O(n^2), M: O(n^2)
    def minSteps(self, n: int) -> int:
        cache = {}

        def helper(count, paste):  # count: num of As on screen, paste: no of As copied
            if count == n:
                return 0
            if count > n:
                # return really big number because this cannot be the answer, n <= 1000
                return 1000
            if (count, paste) in cache:
                return cache[(count, paste)]

            # Paste
            res1 = 1 + helper(count + paste, paste)
            # Copy & Paste, if we just copy here we will end up in infinite loop
            res2 = 2 + helper(count + count, count)
            cache[(count, paste)] = min(res1, res2)
            return cache[(count, paste)]

        if n == 1: return 0
        # we add 1 because the first operation will always be to copy
        return 1 + helper(1, 1)
