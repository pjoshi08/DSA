package org.example.dp1d;

import java.util.ArrayList;
import java.util.List;

public class WordBreak {

    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length()+1];
        for (int i=0; i < s.length()+1; i++) dp[i] = false;
        dp[s.length()] = true;

        for (int i = s.length()-1; i >=0; i--) {
            for (String w: wordDict) {
                if ((i + w.length() <= s.length()) && s.startsWith(w, i))
                    dp[i] = dp[i + w.length()];
                if (dp[i]) break;
            }
        }

        return dp[0];
    }

    public static void main(String[] args) {
        String s = "neetcode";
        List<String> dict = new ArrayList<>();
        dict.add("neet");
        dict.add("leet");
        dict.add("code");
        System.out.println(new WordBreak().wordBreak(s, dict));
    }
}
