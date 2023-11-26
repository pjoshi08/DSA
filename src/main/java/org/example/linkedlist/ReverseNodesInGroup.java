package org.example.linkedlist;

public class ReverseNodesInGroup {

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0, head);
        ListNode groupPrev = dummy;

        while (true) {
            ListNode kth = getKth(groupPrev, k);
            if (kth == null) break;

            ListNode groupNext = kth.next;
            ListNode prev = kth.next, curr = groupPrev.next, temp = null;

            while (curr != groupNext) {
                temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }

            temp = groupPrev.next;
            groupPrev.next = kth;
            groupPrev = temp;
        }

        return dummy.next;
    }

    private ListNode getKth(ListNode node, int k) {
        while (node != null && k > 0) {
            node = node.next;
            k -= 1;
        }

        return node;
    }
}
