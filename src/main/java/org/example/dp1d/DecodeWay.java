package org.example.dp1d;

import java.util.HashMap;
import java.util.Map;

public class DecodeWay {

    Map<Integer, Integer> dp = new HashMap<>();
    int res = 0;
    public int numDecodings(String s) {
        dp.put(s.length(), 1);
        dfs(0, s);
        return res;
    }

    public int numDecodingsDp(String s) {
        dp.put(s.length(), 1);

        for (int i = s.length()-1; i >= 0; i--) {
            if (s.charAt(i) == '0') dp.put(i, 0);
            else dp.put(i, dp.get(i+1));

            if (i+1 < s.length() && (s.charAt(i) == '1'
                    || (s.charAt(i) == '2' &&
                    "0123456".contains(s.subSequence(i+1, i+2))))) {
                dp.put(i, dp.get(i) + dp.get(i+2));
            }
        }

        return dp.get(0);
    }

    // T = O(n), M = O(1)
    private int dfs(int i, String s) {
        if (dp.containsKey(i)) return dp.get(i);
        if (s.charAt(i) == '0') return 0;

        res = dfs(i+1, s);
        if (i+1 < s.length() && (s.charAt(i) == '1'
                || (s.charAt(i) == '2' &&
                "0123456".contains(s.subSequence(i+1, i+2))))) {
            res += dfs(i+2, s);
        }
        dp.put(i, res);
        return res;
    }



    public static void main(String[] args) {
        String s = "121";
        //String s = "1";
        //System.out.println(new DecodeWay().numDecodings(s));
        System.out.println(new DecodeWay().numDecodingsDp(s));
    }
}
