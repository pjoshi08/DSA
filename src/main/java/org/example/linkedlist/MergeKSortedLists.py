from typing import Optional, List

from org.example.linkedlist.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0: return None

        def merge(l, r):
            if l == r: return lists[l]
            if l + 1 == r: return self.mergeLists(lists[l], lists[r])

            m = l + (r - l) // 2
            left = merge(l, m)
            right = merge(m + 1, r)
            return self.mergeLists(left, right)

        return merge(0, len(lists) - 1)

    def mergeLists(self, list1, list2):
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return dummy.next
