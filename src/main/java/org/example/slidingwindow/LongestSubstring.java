package org.example.slidingwindow;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LongestSubstring {

    // 7ms, 43.6MB
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) return 0;
        if (s.length() == 1) return 1;

        int l = 0, maxCount = 0;
        Set<Character> set = new HashSet<>();

        for (int r=0; r < s.length(); r++) {
            while (set.contains(s.charAt(r))) {
                set.remove(s.charAt(l));
                l += 1;
            }

            set.add(s.charAt(r));
            maxCount = Math.max(maxCount, r - l + 1);
        }

        return maxCount;
    }

    // Accepted solution but slower(70 ms, 44.3MB)
    public int lengthOfLongestSubstring1(String s) {
        if (s.isEmpty()) return 0;
        if (s.length() == 1) return 1;

        int count = 0, maxCount = 0;
        Map<Character, Integer> map = new HashMap<>();
        char[] arr = s.toCharArray();
        int i=0;
        while (i < arr.length) {
            if (!map.containsKey(arr[i])) {
                count++;
                maxCount = Math.max(count, maxCount);
            } else {
                i = map.get(arr[i]) + 1;
                map.clear();
                count = 1;
            }
            map.put(arr[i], i);
            i++;
        }

        return maxCount;
    }

    public static void main(String[] args) {
        LongestSubstring obj = new LongestSubstring();
        //String s = "abcabcbb";
        //String s = "pwwkew";
        //String s = "bbbbbbbb";
        String s = "dvdf";
        System.out.println(obj.lengthOfLongestSubstring(s));
    }
}
