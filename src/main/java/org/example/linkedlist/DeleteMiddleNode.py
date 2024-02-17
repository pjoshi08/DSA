from typing import Optional

from org.example.linkedlist.ListNode import ListNode

# Delete the Middle Node of a Linked List:
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We need dummy to handle the edge case of a LL with just one node,
        # we return empty LL in that case
        dummy = prev = ListNode(-1)
        slow = fast = head
        prev.next = slow
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return dummy.next
