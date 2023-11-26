package org.example.backtrack;

import java.util.ArrayList;
import java.util.List;

public class Subsets {

    // T = O(n * 2^n)
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> subset = new ArrayList<>();
    public List<List<Integer>> subsets(int[] nums) {
        dfs(0, nums);
        return res;
    }

    private void dfs(int i, int[] nums) {
        if (i >= nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }

        // Decision to add nums[i]
        subset.add(nums[i]);
        dfs(i+1, nums);

        // Decision to not add nums[i]
        subset.remove(subset.size()-1);
        dfs(i+1, nums);
    }
}
