package org.example.dp1d;

public class LongestPalindromicSubStr {

    public String longestPalindrome(String s) {
        if (s.length() == 1) return s;
        String res = "";
        int resLen = 0;

        for (int i=0; i<s.length(); i++) {
            int l = i, r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if ((r - l + 1) > resLen) {
                    res = s.substring(l, r+1);
                    resLen = r - l + 1;
                }
                l -= 1;
                r += 1;
            }

            l = i; r = i+1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if ((r - l + 1) > resLen) {
                    res = s.substring(l, r+1);
                    resLen = r - l + 1;
                }
                l -= 1;
                r += 1;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        //String s = "babad";
        String s = "cbbd";
        System.out.println(new LongestPalindromicSubStr().longestPalindrome(s));
    }
}
