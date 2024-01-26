from org.example.linkedlist.ListNode import ListNode


class Solution:
    def reverseList(self, head):
        if head is None: return head
        curr, next = head, head.next
        prev = None
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        return prev


obj = Solution()
five = ListNode(5, None)
four = ListNode(4, five)
three = ListNode(3, four)
two = ListNode(2, three)
head = ListNode(1, two)

print(obj.reverseList(head))