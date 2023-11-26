package org.example.blind;

public class RevLinkedList {
    // T = O(n), M = O(1)
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;
        ListNode next, curr = head, prev = null;

        while(curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }

    // T = O(n), M = O(n)
    public ListNode revListRecursive(ListNode head) {
        if (head == null) return null;
        ListNode newHead = head;
        if (head.next != null) {
            newHead = revListRecursive(head.next);
            head.next.next = head;
        }
        head.next = null;
        return newHead;
    }

    public ListNode getListNodeEx1() {
        ListNode node5 = new ListNode(5);
        ListNode node4 = new ListNode(4, node5);
        ListNode node3 = new ListNode(3, node4);
        ListNode node2 = new ListNode(2, node3);
        return new ListNode(1, node2);
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        ListNode curr = this;
        ListNode currNext = next;
        while (currNext != null) {
            builder.append(curr.val)
                    .append("->")
                    .append(curr.next);
            curr = curr.next;
            currNext = curr.next;
        }

        return builder.toString();
    }
}
