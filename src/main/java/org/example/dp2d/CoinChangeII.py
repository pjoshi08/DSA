class Solution(object):
    # dp solution with two rows, 63%
    # O(n * m) time, O(m) space
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]

    # dp solution, 41% on leetcode, better than caching solution
    # O(n * m) time, O(n * m) space
    def change4(self, amount, coins):
        coinsLen = len(coins)
        dp = [[0 for i in range(coinsLen + 1)] for j in range(amount + 1)]
        dp[0] = [1] * (coinsLen + 1)

        for a in range(1, amount + 1):
            for i in range(coinsLen - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

    # normal dfs cache solution, 25% on leetcode
    def change3(self, amount, coins):
        cache = {}  # {(i, amount): combinations}
        coinsLen = len(coins)

        def dfs(i, amt):
            if amt == amount: return 1
            if amt > amount or i >= coinsLen: return 0
            if (i, amt) in cache: return cache[(i, amt)]

            cache[(i, amt)] = dfs(i, amt + coins[i]) + dfs(i + 1, amt)
            return cache[(i, amt)]

        return dfs(0, 0)

    def change2(self, amount, coins):
        dp = {}  # key=amount, val=combinations
        minDenom = min(coins)

        def dfs(subAmount):
            if subAmount == 0:
                return 1
            if subAmount in dp:
                return dp[subAmount]
            if subAmount < minDenom:
                return 0

            count = 0
            for c in coins:
                if subAmount >= c:
                    count += dfs(subAmount - c)
                    dp[subAmount] = count
            return dp[subAmount]

        return dfs(amount)


sol = Solution()
coins = [1, 2, 5]
count = sol.change(5, coins)
print(count)