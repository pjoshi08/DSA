# Given the head of a linked list, find all the values that appear more than once in the list
# and delete the nodes that have any of those values.
#
# Return the linked list after the deletions.
from org.example.linkedlist.ListNode import ListNode


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = {}
        dummy = ListNode(0, head)
        cur = dummy.next

        while cur:
            freq[cur.val] = 1 + freq.get(cur.val, 0)
            cur = cur.next

        cur = dummy.next
        prev = dummy

        while cur:
            if freq[cur.val] > 1:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next

        return dummy.next
