package org.example.arrays;

import java.util.*;

public class LongestConsecutiveInts {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        Set<Integer> set = new HashSet<>();

        for (int num: nums) set.add(num);

        int maxCount=1;
        for (int num: set) {
            if (!set.contains(num-1)) {
                int len = 1;
                while (set.contains(num + len)) {
                    len += 1;
                }

                maxCount = Math.max(maxCount, len);
            }
        }

        return maxCount;
    }
}
