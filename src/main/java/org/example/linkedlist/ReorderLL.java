package org.example.linkedlist;

public class ReorderLL {

    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head.next;
        if (slow.next == null) return;

        // To find the middle point
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse the second half of the LL
        ListNode second = slow.next;
        slow.next = null;
        ListNode prev = null, temp;
        while (second != null) {
            temp = second.next;
            second.next = prev;
            prev = second;
            second = temp;
        }

        second = prev;
        ListNode first = head;
        while (second != null) {
            ListNode temp1 = first.next, temp2 = second.next;
            first.next = second;
            second.next = temp1;
            first = temp1;
            second = temp2;
        }
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        ListNode sec = new ListNode(2);
        ListNode third = new ListNode(3);
        ListNode fourth = new ListNode(4);
        ListNode fifth = new ListNode(5);
        head.next = sec;
        sec.next = third;
        third.next = fourth;
        fourth.next = fifth;

        new ReorderLL().reorderList(head);
        System.out.println(head);
    }
}
