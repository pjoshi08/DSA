package org.example.twopointers;

public class TwoSumII {
    public int[] twoSum(int[] numbers, int target) {
        int idx1=0, idx2=numbers.length-1;

        for (int i=0; i<numbers.length; i++) {
            if (numbers[idx1] + numbers[idx2] == target) {
                return new int[]{++idx1, ++idx2};
            } else if (numbers[idx1] + numbers[idx2] < target) {
                idx1++;
            } else if (numbers[idx1] + numbers[idx2] > target) {
                idx2--;
            }
        }

        return new int[]{++idx1, ++idx2};
    }
}
