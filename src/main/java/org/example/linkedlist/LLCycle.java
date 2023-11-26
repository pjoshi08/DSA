package org.example.linkedlist;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class LLCycle {

    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        ListNode slow = head, fast = head.next;
        while (fast != null) {
            if (fast == slow) return true;

            slow = slow.next;
            fast = fast.next.next;
        }

        return false;
    }

    public boolean hasCycle2(ListNode head) {
        if (head == null) return false;
        HashSet<ListNode> nodes = new HashSet<>();
        ListNode next = head.next;
        while (next != null) {
            if (nodes.contains(next)) return true;

            nodes.add(next);
            next = next.next;
        }

        return false;
    }
}
