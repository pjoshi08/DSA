package org.example.dp1d;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class PartitionEqSubsetSum {

    // Better solution, T = 20ms
    Boolean[][] dp;
    public boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        if (sum % 2 == 1) return false;

        sum /= 2;
        dp = new Boolean[nums.length][sum+1];

        return canPartition(nums, sum, 0);
    }

    private boolean canPartition(int[] nums, int sum, int index) {
        if (sum == 0) return true;
        if (index >= nums.length || sum < 0) return false;
        if (dp[index][sum] != null) return dp[index][sum];

        var value = canPartition(nums, sum - nums[index], index + 1) ||
                canPartition(nums, sum, index + 1);
        dp[index][sum] = value;

        return value;
    }

    // Slow, T = 163ms
    public boolean canPartition2(int[] nums) {
        int sum = 0;
        for (int n: nums) sum += n;
        if (sum % 2 == 1) return false;

        int target = sum / 2;
        Set<Integer> dp = new HashSet<>();
        dp.add(0);
        for (int i = nums.length-1; i >= 0; i--) {
            Set<Integer> newDp = new HashSet<>();
            for (int t: dp) {
                if (t + nums[i] == target) return true;
                newDp.add(t + nums[i]);
                newDp.add(t);
            }

            dp = newDp;
        }

        return dp.contains(target);
    }

    public static void main(String[] args) {
        int[] nums = {1,5,11,5};
        System.out.println(new PartitionEqSubsetSum().canPartition(nums));
    }
}

class Solution {
    public boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        if (sum % 2 != 0) {
            return false;
        }

        sum /= 2;

        return canPartition(nums, sum, 0, new Boolean[nums.length][sum + 1]);
    }

    private boolean canPartition(int[] nums, int sum, int index, Boolean[][] memo) {
        if (sum == 0) {
            return true;
        }
        if (index >= nums.length || sum < 0) {
            return false;
        }
        if (memo[index][sum] != null) {
            return memo[index][sum];
        }

        var value =  canPartition(nums, sum - nums[index], index + 1, memo) ||
                canPartition(nums, sum, index + 1, memo);

        memo[index][sum] = value;

        return value;
    }
}
