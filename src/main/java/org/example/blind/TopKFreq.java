package org.example.blind;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TopKFreq {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        ArrayList<Integer>[] frequency = new ArrayList[nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            count.put(nums[i], 1 + count.getOrDefault(nums[i], 0));
            frequency[i] = new ArrayList<>();
        }
        frequency[nums.length] = new ArrayList<>();

        for (Map.Entry entry: count.entrySet()) {
            frequency[(int) entry.getValue()].add((int) entry.getKey());
        }

        int[] result = new int[k];
        int index = 0;
        for (int i = nums.length; i >= 1; i--) {
            for (int n: frequency[i]) {
                result[index++] = n;
                if (index == k) {
                    return result;
                }

            }
        }

        return result;
    }
}
