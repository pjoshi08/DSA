package org.example.blind;

import java.util.Arrays;
import java.util.HashMap;

public class Anagram {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character, Integer> sCount = new HashMap<>();
        HashMap<Character, Integer> tCount = new HashMap<>();

        for (Character c: s.toCharArray()) {
            sCount.put(c, 1 + sCount.getOrDefault(c, 0));
        }
        for (Character c: t.toCharArray()) {
            tCount.put(c, 1 + tCount.getOrDefault(c, 0));
        }

        for (Character c: s.toCharArray()) {
            if (!sCount.get(c).equals(tCount.getOrDefault(c, 0)))
                return false;
        }

        return true;
    }

    public boolean isAnagram2(String s, String t) {
        Arrays.sort(s.toCharArray());
        Arrays.sort(t.toCharArray());
        return s.equals(t);
    }
}
