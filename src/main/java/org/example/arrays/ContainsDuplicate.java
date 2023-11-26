package org.example.arrays;

import java.util.HashMap;
import java.util.Map;

public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {

        Map<Integer, Boolean> map = new HashMap<>();
        for (int num: nums) {
            if (map.containsKey(num)) return true;

            map.put(num, true);
        }

        return false;
    }
}
