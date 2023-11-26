package org.example.backtrack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CombinationSumII {

    List<List<Integer>> res = new ArrayList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        dfs(0, candidates, target, 0, new ArrayList<>());
        return res;
    }

    private void dfs(int i, int[] candidates, int target, int total, List<Integer> list) {
        if (total == target) {
            res.add(new ArrayList<>(list));
            return;
        }

        if (i == candidates.length || total > target) return;

        list.add(candidates[i]);
        dfs(i+1, candidates, target, total + candidates[i], list);

        list.remove(list.size()-1);
        while (i+1 < candidates.length && candidates[i] == candidates[i+1])
            i += 1;
        dfs(i+1, candidates, target, total, list);
    }
}
