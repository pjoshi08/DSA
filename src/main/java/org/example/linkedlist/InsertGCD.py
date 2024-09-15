# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from org.example.linkedlist.ListNode import ListNode


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        right = head.next
        left = head
        while right:
            gcd_val = self.gcd(left.val, right.val)
            gcd_node = ListNode(gcd_val, right)
            left.next = gcd_node
            left = right
            right = right.next
        return dummy.next

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)