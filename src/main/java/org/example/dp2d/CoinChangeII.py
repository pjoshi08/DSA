class Solution(object):

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

    def change2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int (number of combinations)
        """
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
coins = [1,2,5]
count = sol.change(5, coins)
print(count)