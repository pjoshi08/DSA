package org.example.slidingwindow;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class LongestRepeatingSubStrReplacement {

    // O(26n)
    public int characterReplacement(String s, int k) {
        // hashmap to count frequency of char occurrences
        Map<Character, Integer> count = new HashMap<>();

        // Logic: Length of Window - Max Freq of char in window <= k
        int l=0, res=0;
        for (int r=0; r < s.length(); r++) {
            count.put(s.charAt(r), count.getOrDefault(s.charAt(r), 0) + 1);

            while ((r - l + 1) - Collections.max(count.values()) > k) {
                count.put(s.charAt(l), count.get(s.charAt(l)) - 1);
                l += 1;
            }

            res = Math.max(res, r - l + 1);
        }

        return res;
    }

    // Almost 3 times faster; O(n)
    public int characterReplacement2(String s, int k) {
        // hashmap to count frequency of char occurrences
        Map<Character, Integer> count = new HashMap<>();

        // Logic: Length of Window - Max Freq of char in window <= k
        int l=0, res=0, maxF=0;
        for (int r=0; r < s.length(); r++) {
            count.put(s.charAt(r), count.getOrDefault(s.charAt(r), 0) + 1);
            maxF = Math.max(maxF, count.get(s.charAt(r)));

            while ((r - l + 1) - maxF > k) {
                count.put(s.charAt(l), count.get(s.charAt(l)) - 1);
                l += 1;
            }

            res = Math.max(res, r - l + 1);
        }

        return res;
    }

    // 6 ms, 3.5 times faster than
    public int characterReplacement3(String s, int k) {
        int chararr[] = new int[26];
        int n = s.length();
        int start = 0;
        int ans = 0;
        int maxi = 0;

        for(int end=0; end<n; end++){
            chararr[s.charAt(end)-'A']++;
            maxi=Math.max(maxi,chararr[s.charAt(end)-'A']);

            while(end - start - maxi + 1 > k){
                chararr[s.charAt(start)-'A']--;
                start++;
            }
            ans = Math.max(ans,end - start + 1);
        }
        return ans;
    }
}
