from typing import Optional

from org.example.linkedlist.ListNode import ListNode


# Swap Nodes in pairs: https://leetcode.com/problems/swap-nodes-in-pairs/
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev)
            if not kth: break

            groupNext = kth.next
            curr, prev = groupPrev.next, kth.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, node, k=2):
        while node and k > 0:
            node = node.next
            k -= 1
        return node
