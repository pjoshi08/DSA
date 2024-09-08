# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, List

from org.example.linkedlist.ListNode import ListNode


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        split_size = size // k
        remaining_parts = size % k
        cur = head

        for i in range(k):
            new_part = ListNode(0)
            tail = new_part
            cur_size = split_size

            if remaining_parts > 0:
                remaining_parts -= 1
                cur_size += 1
            for _ in range(cur_size):
                tail.next = ListNode(cur.val)
                tail = tail.next
                cur = cur.next
            res[i] = new_part.next
        return res
