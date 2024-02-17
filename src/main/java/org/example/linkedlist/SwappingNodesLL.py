from typing import Optional

from org.example.linkedlist.ListNode import ListNode

# Swapping Nodes LL: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/1177068207/

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = pre_left = pre_right = ListNode(0, head)
        left = right = head
        for i in range(k - 1):
            pre_left = left
            left = left.next

        null_checker = left
        while null_checker.next:
            pre_right = right
            right = right.next
            null_checker = null_checker.next
        if left == right: return head

        pre_left.next, pre_right.next = right, left
        left.next, right.next = right.next, left.next

        return dummy.next


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
obj = Solution()
print(obj.swapNodes(n1, 2))