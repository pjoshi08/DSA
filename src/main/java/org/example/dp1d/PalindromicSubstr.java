package org.example.dp1d;

import java.util.ArrayList;
import java.util.List;

public class PalindromicSubstr {

    //List<String> res = new ArrayList<>();
    int count=0;
    public int countSubstrings(String s) {

        for (int i=0; i < s.length(); i++) {
            int l, r;
            // Odd len
            l = i; r = i;
            palindromeDp(s, l, r);

            // Even len
            l = i; r = i+1;
            palindromeDp(s, l, r);
        }

        return count;
    }

    private void palindromeDp(String s, int l, int r) {
        while(l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            //res.add(s.substring(l, r+1));
            count += 1;
            l -= 1; r += 1;
        }
    }

    public static void main(String[] args) {
        //String s = "aaa";
        String s = "abc";
        System.out.println(new PalindromicSubstr().countSubstrings(s));
    }
}
