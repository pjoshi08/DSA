package org.example.binarysearch;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TimeMap2 {
    Map<String, List<Data>> map;

    public TimeMap2() {
        map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        if (!map.containsKey(key)) {
            map.put(key, new ArrayList<>());
        }
        map.get(key).add(new Data(value, timestamp));
    }

    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) return "";

        List<Data> list = map.get(key);
        int left = 0;
        int right = list.size() - 1;

        while (left < right) {
            int mid = left + (right - left)/2;
            if (list.get(mid).timestamp == timestamp) return list.get(timestamp).value;
            if (timestamp > list.get(mid).timestamp) {
                if (list.get(mid+1).timestamp > timestamp) return list.get(mid).value;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return list.get(left).timestamp <= timestamp ? list.get(left).value : "";
    }

    public static void main(String[] args) {
        TimeMap timeMap = new TimeMap();
        timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
        System.out.println(timeMap.get("foo", 1));         // return "bar"
        System.out.println(timeMap.get("foo", 3));         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
        timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
        System.out.println(timeMap.get("foo", 4));         // return "bar2"
        System.out.println(timeMap.get("foo", 5));         // return "bar2"
    }
}

class Data {
    String value;
    int timestamp;

    public Data(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }
}
