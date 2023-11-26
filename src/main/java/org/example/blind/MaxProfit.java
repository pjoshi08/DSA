package org.example.blind;

public class MaxProfit {

    public int maxProfit(int[] prices) {
        int maxProfit = 0;

        int left = 0, right = 1;
        int profit;
        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            } else {
                left = right;
            }

            right += 1;
        }

        return maxProfit;
    }
}
