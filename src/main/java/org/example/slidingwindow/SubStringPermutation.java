package org.example.slidingwindow;

import java.util.Arrays;

public class SubStringPermutation {
    public boolean checkInclusion(String s1, String s2) {
        int[] s1Freq = new int[26], s2Freq = new int[26];
        for (int i=0; i < s1.length(); i++)
            s1Freq[s1.charAt(i) - 'a']++;
        int l = 0, window = s1.length();
        boolean res = false;

        for (int r=0; r < s2.length(); r++) {
            s2Freq[s2.charAt(r) - 'a']++;

            while ((r - l + 1) > window) {
                s2Freq[s2.charAt(l) - 'a']--;
                l += 1;
            }

            if ((r - l + 1) == window) {
                 res = Arrays.equals(s1Freq, s2Freq);
                 if (res) return res;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        String s1 = "ab", s2 = "eidboaooo";
        System.out.println(new SubStringPermutation().checkInclusion(s1, s2));
    }
}
