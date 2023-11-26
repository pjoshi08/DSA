package org.example.binarysearch;

// This solution takes 128MB(5.02%) space and 109ms time(99.75%)
public class TimeMap {

    private String[] keys;
    private String[] values;
    private int size;

    public TimeMap() {
        keys = new String[1];
        values = new String[1];
        size = keys.length;
    }

    public void set(String key, String value, int timestamp) {
        if (timestamp >= size) {
            ensureCapacity(timestamp);
        }

        keys[timestamp] = key;
        values[timestamp] = value;
    }

    public String get(String key, int timestamp) {
        if (timestamp >= keys.length) {
            // search from the end
            timestamp = keys.length - 1;
        }

        return getLastValue(key, timestamp);
    }

    private void ensureCapacity(int capacity) {
        String[] oldKeys = keys;
        String[] oldValues = values;
        keys = new String[2 * capacity + 1];
        values = new String[2 * capacity + 1];
        System.arraycopy(oldKeys, 0, keys, 0, size);
        System.arraycopy(oldValues, 0, values, 0, size);
        size = keys.length;
    }

    private String getLastValue(String key, int timestamp) {
        for (int i = timestamp; i >= 0; i--) {
            if (keys[i] == null) continue;
            if (keys[i].equals(key)) return values[i];
        }

        return "";
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
