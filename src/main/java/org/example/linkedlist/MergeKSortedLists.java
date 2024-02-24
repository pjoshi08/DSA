package org.example.linkedlist;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class MergeKSortedLists {

    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        return merge(lists, 0, lists.length-1);
    }

    private ListNode merge(ListNode[] lists, int start, int end) {
        if (start == end) return lists[start];
        if (start + 1 == end) return mergeLists(lists[start], lists[end]);

        int mid = start + (end - start)/2;
        ListNode left = merge(lists, start, mid);
        ListNode right = merge(lists, mid+1, end);
        return mergeLists(left, right);
    }

    private ListNode mergeLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;

        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }

        if (l1 != null) {
            tail.next = l1;
        }
        if (l2 != null) {
            tail.next = l2;
        }

        return dummy.next;
    }

    // Exceeding time limit
    public ListNode mergeKLists3(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;


        while (lists.length > 1) {
            ListNode[] mergedLists = new ListNode[(lists.length/2) + 1];
            for (int i=0; i < lists.length; i = i+2) {
                ListNode l1 = lists[0], l2;
                if (i+1 < lists.length) {
                    l2 = lists[1];
                } else {
                    l2 = null;
                }

                mergedLists[i/2] = mergeLists(l1, l2);
            }
            lists = mergedLists;
        }

        return lists[0];
    }



    public ListNode mergeKLists2(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;

        TreeMap<Integer, List<ListNode>> map = new TreeMap<>();
        for (ListNode node: lists) {
            while (node != null) {
                if (map.containsKey(node.val)) {
                    map.get(node.val).add(node);
                } else {
                    List<ListNode> list = new ArrayList<>();
                    list.add(node);
                    map.put(node.val, list);
                }

                node = node.next;
            }
        }

        ListNode dummy = new ListNode();
        ListNode head = dummy;
        for (Map.Entry<Integer, List<ListNode>> entry : map.entrySet()) {
            for (ListNode node: entry.getValue()) {
                head.next = new ListNode(node.val);
                head = head.next;
            }
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode node = new ListNode();
        ListNode n1 = new ListNode(2);
        node.next = n1;
        n1.next = new ListNode(5);

        ListNode[] lists = {node};
        System.out.println(new MergeKSortedLists().mergeKLists(lists));
    }
}
