from typing import Optional

from org.example.linkedlist.ListNode import ListNode

# Linked List Cycle II: https://leetcode.com/problems/linked-list-cycle-ii/
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        nodes = set()
        while node:
            if node in nodes: return node
            nodes.add(node)
            node = node.next
        return None
