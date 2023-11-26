package org.example.dp1d;

public class MaxProdSubarr {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int currMax = 1, currMin = 1;

        for (int n: nums) {
            int temp = currMax * n;
            currMax = Math.max(Math.max(currMax * n, currMin * n), n);
            currMin = Math.min(Math.min(temp, currMin * n), n);
            res = Math.max(currMax, res);
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = {2,3,-2,4};
        System.out.println(new MaxProdSubarr().maxProduct(nums));
    }
}
