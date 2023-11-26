package org.example.twopointers;

public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        if (s.isEmpty()) return true;

        int i=0, j=s.length()-1;
        char[] sArray = s.toCharArray();
        for (; i <= (s.length()-1) / 2 ; i++, j--) {
            if (sArray[i] != sArray[j]) return false;
        }

        return true;
    }

}
