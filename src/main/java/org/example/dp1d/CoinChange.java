package org.example.dp1d;

public class CoinChange {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        dp[0] = 0;
        for (int i=1; i < amount+1; i++) dp[i] = amount+1;

        for (int amt=1; amt < amount+1; amt++) {
            for (int c: coins) {
                if (amt - c >= 0)
                    dp[amt] = Math.min(dp[amt], 1 + dp[amt - c]);
            }
        }

        if (dp[amount] != amount+1)
            return dp[amount];
        else
            return -1;
    }

    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int amount = 11;
        System.out.println(new CoinChange().coinChange(coins, amount));
    }
}
