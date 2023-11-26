package org.example.blind;

import java.util.Arrays;
import java.util.HashMap;

public class MissingNumber {

    public int missingNumber(int[] nums) {
        int result = nums.length;

        for (int i = 0; i < nums.length; i++) {
            result ^= i ^ nums[i];
            //result ^= nums[i];
        }

        return result;
    }

    public int missingNumber1(int[] nums) {
        int result = nums.length;

        for (int i = 0; i < nums.length; i++) {
            result += (i - nums[i]);
        }

        return result;
    }

    /** O(n) time + O(n) memory - better soln */
    public int missingNumber2(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i <= nums.length; i++) {
            map.put(i, 0);
        }

        for (int num : nums) {
            map.remove(num);
        }

        return (int) map.keySet().toArray()[0];
    }

    /** O(n log n) time - bad solution */
    public int missingNumber3(int[] nums) {
        Arrays.sort(nums);

        int i;
        for (i = 0; i < nums.length; i++) {
            if (i != nums[i]) return i;
        }

        return i;
    }
}
