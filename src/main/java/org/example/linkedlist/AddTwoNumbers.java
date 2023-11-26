package org.example.linkedlist;

public class AddTwoNumbers {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode cur = dummy;

        int carry=0;
        while (l1 != null || l2 != null || carry > 0) {
            int d1 = l1 != null ? l1.val : 0;
            int d2 = l2 != null ? l2.val : 0;

            // calculate new digit
            int sum = d1 + d2 + carry;
            carry = sum / 10;
            sum = sum % 10;
            cur.next = new ListNode(sum);

            // Shift pointers
            cur = cur.next;
            l1 = l1 != null ? l1.next : null;
            l2 = l2 != null ? l2.next : null;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode h = new ListNode(2);
        ListNode sec = new ListNode(4);
        ListNode third = new ListNode(3);
        h.next = sec; sec.next = third;

        ListNode h2 = new ListNode(5);
        ListNode sec2 = new ListNode(6);
        ListNode third2 = new ListNode(4);
        h2.next = sec2; sec2.next = third2;

        System.out.println(new AddTwoNumbers().addTwoNumbers(h, h2));
    }

}
