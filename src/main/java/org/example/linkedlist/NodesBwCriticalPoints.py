# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from typing import List, Optional

from org.example.linkedlist.ListNode import ListNode


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]

        firstPoint, prevPoint, n = 0, 0, 1
        prev, cur = head, head.next
        minDiff = float('inf')

        while cur.next:
            if ((prev.val < cur.val > cur.next.val) or
                    (prev.val > cur.val < cur.next.val)):
                if prevPoint == 0:  # first critical point
                    firstPoint = n
                else:
                    minDiff = min(minDiff, n - prevPoint)
                prevPoint = n
            cur = cur.next
            n += 1

        if minDiff != float('inf'):
            res = [minDiff, prevPoint - firstPoint]

        return res
