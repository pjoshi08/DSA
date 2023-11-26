package org.example.arrays;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GroupAnagrams {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<List<Integer>, List<String>> map = new HashMap<>();

        for (String s : strs) {
            List<Integer> count = new ArrayList() {{ for (int i=0; i < 26; i++) add(0); }};
            for (char c: s.toCharArray()) {
                count.set(c - 'a', count.get(c - 'a') + 1);
            }

            List<String> list = map.getOrDefault(count, new ArrayList<>());
            list.add(s);
            map.put(count, list);
        }

        return new ArrayList<>(map.values());
    }
}
