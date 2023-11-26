package org.example.backtrack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SubsetsII {

    List<List<Integer>> res = new ArrayList<>();
    List<Integer> subset = new ArrayList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        dfs(0, nums);
        return res;
    }

    private void dfs(int i, int[] nums) {
        if (i >= nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[i]);
        dfs(i + 1, nums);

        subset.remove(subset.size() - 1);
        while (i + 1 < nums.length && nums[i] == nums[i + 1])
            i += 1;
        dfs(i + 1, nums);
    }

    public static void main(String[] args) {
        //int[] nums = {1,2,2};
        int[] nums = {0};
        System.out.println(new SubsetsII().subsetsWithDup(nums));
    }
}
