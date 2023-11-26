package org.example.linkedlist;

public class ReverseLinkedList {

    // Iterative solution; O(n), M(1)
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head, next;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }

    // O(n), M(n)
    public ListNode reverseRecursive(ListNode head) {
        if (head == null) return null;

        ListNode newHead = head;
        if (head.next != null) {
            newHead = reverseRecursive(head.next);
            head.next.next = head;
        }
        head.next = null;

        return newHead;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode sec = new ListNode(2);
        ListNode third = new ListNode(3);
        head.next = sec;
        sec.next = third;

        System.out.println(new ReverseLinkedList().reverseRecursive(head));
    }
}
