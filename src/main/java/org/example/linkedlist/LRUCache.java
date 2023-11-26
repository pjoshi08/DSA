package org.example.linkedlist;

import java.util.HashMap;
import java.util.Map;

public class LRUCache {

    private final int capacity;
    private Node left, right;
    private final Map<Integer, Node> cache;
    public LRUCache(int capacity) {
        this.capacity = capacity;

        // Hashmap to map Key to Node
        cache = new HashMap<>();
        left = new Node(0, 0);
        right = new Node(0, 0);
        left.next = right;
        right.prev = left;
    }

    public int get(int key) {
        if (cache.containsKey(key)) {
            // Update LRU
            delete(cache.get(key));
            insert(cache.get(key));
            return cache.get(key).val;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) delete(cache.get(key));
        cache.put(key, new Node(key, value));
        insert(cache.get(key));

        if (cache.size() > capacity) {
            Node lru = left.next;
            delete(lru);
            cache.remove(lru.key);
        }
    }

    private void insert(Node node) {
        Node prev = right.prev;
        Node next = right;
        prev.next = node;
        next.prev = node;
        node.prev = prev;
        node.next = next;
    }

    private void delete(Node node) {
        Node prev = node.prev;
        Node next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    class Node {
        int key, val;
        Node prev, next;

        public Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }
}
