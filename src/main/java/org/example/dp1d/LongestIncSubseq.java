package org.example.dp1d;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class LongestIncSubseq {

    public int lengthOfLIS(int[] nums) {
        List<Integer> LIS = new ArrayList<>();
        for (int i=0; i < nums.length; i++) LIS.add(1);

        for (int i = nums.length-1; i >= 0; i--) {
            for (int j = i+1; j < nums.length; j++)
                if (nums[i] < nums[j])
                    LIS.set(i, Math.max(LIS.get(i), 1 + LIS.get(j)));
        }

        return Collections.max(LIS);
    }

    public static void main(String[] args) {
        int[] nums = {1,2,4,3};
        System.out.println(new LongestIncSubseq().lengthOfLIS(nums));
    }
}
