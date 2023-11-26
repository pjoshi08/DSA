package org.example.dp1d;

import java.util.Arrays;

public class HouseRobberII {

    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        return Math.max(
                helper(Arrays.copyOfRange(nums, 0, nums.length-1)),
                helper(Arrays.copyOfRange(nums, 1, nums.length))
        );
    }

    private int helper(int[] nums) {
        int rob1 = 0, rob2 = 0, temp;
        for (int n : nums) {
            temp = Math.max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }

    public static void main(String[] args) {
        //int[] nums = {2,3,2};
        //int[] nums = {1, 2, 3, 1};
        int[] nums = {1, 2, 1, 1};
        System.out.println(new HouseRobberII().rob(nums));
    }
}
