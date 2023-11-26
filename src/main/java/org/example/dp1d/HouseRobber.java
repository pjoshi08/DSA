package org.example.dp1d;

public class HouseRobber {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        int rob1=0, rob2=0, temp;
        for (int n: nums) {
            temp = Math.max(n + rob1, rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return rob2;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,3,1};
        System.out.println(new HouseRobber().rob(nums));
    }
}
