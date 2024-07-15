from typing import Optional, List

from org.example.linkedlist.ListNode import ListNode


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        cur, prev = head, dummy

        while cur:
            if cur.val in nums:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next
