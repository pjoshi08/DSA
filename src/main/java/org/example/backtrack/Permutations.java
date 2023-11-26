package org.example.backtrack;

import java.util.*;

public class Permutations {
    public List<List<Integer>> permute(int[] nums) {
        return dfs(new ArrayList<Integer>() {{
            for (int i : nums) add(i);
        }});
    }

    private List<List<Integer>> dfs(List<Integer> nums) {
        List<List<Integer>> res = new ArrayList<>();

        if (nums.size() == 1) {
            res.add(new ArrayList<>(nums));
            return res;
        }

        int len = nums.size();
        for (int i = 0; i < len; i++) {
            int n = nums.remove(0);
            List<List<Integer>> perms = dfs(nums);

            for (List<Integer> perm : perms) {
                perm.add(n);
            }

            res.addAll(perms);
            nums.add(n);
        }

        return res;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        System.out.println(new Permutations().permute(nums));
    }
}
