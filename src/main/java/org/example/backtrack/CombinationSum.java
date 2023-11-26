package org.example.backtrack;

import java.util.ArrayList;
import java.util.List;

public class CombinationSum {

    private List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        dfs(0, new ArrayList<>(), 0, target, candidates);
        return res;
    }

    private void dfs(int i, List<Integer> curr, int total, int target, int[] candidates) {
        if (total == target) {
            res.add(new ArrayList<>(curr));
            return;
        }

        if (i >= candidates.length || total > target) return;

        curr.add(candidates[i]);
        dfs(i, curr, total + candidates[i], target, candidates);

        curr.remove(curr.size()-1);
        dfs(i+1, curr, total, target, candidates);
    }
}
