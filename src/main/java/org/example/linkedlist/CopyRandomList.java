package org.example.linkedlist;

import java.util.HashMap;
import java.util.Map;

public class CopyRandomList {
    public Node copyRandomList(Node head) {
        Map<Node, Node> map = new HashMap<>();

        Node cur = head;
        Node copy;
        while (cur != null) {
            copy = new Node(cur.val, null, null);
            map.put(cur, copy);
            cur = cur.next;
        }

        cur = head;
        while (cur != null) {
            copy = map.get(cur);
            copy.next = map.getOrDefault(cur.next, null);
            copy.random = map.getOrDefault(cur.random, null);
            cur = cur.next;
        }

        return map.get(head);
    }
}
