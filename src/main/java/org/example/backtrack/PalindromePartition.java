package org.example.backtrack;

import java.util.ArrayList;
import java.util.List;

public class PalindromePartition {

    private List<List<String>> res = new ArrayList<>();
    public List<List<String>> partition(String s) {
        dfs(0, s, new ArrayList<>());
        return res;
    }

    private void dfs(int i, String s, List<String> list) {
        if (i >= s.length()) {
            res.add(new ArrayList<>(list));
            return;
        }

        for (int j=i; j < s.length(); j++) {
            if (isPalindrome(s, i, j)) {
                list.add(s.substring(i, j+1));
                dfs(j+1, s, list);
                list.remove(list.size()-1);
            }
        }
    }

    private boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) return false;
            l += 1;
            r -= 1;
        }
        return true;
    }
}
