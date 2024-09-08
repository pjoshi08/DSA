from typing import Optional

from org.example.linkedlist.ListNode import ListNode
from org.example.tree.TreeNode import TreeNode


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if self.helper(head, root):
            return True
        if not root:
            return False
        return (
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right)
        )

    def helper(self, list_node, tree_node):
        if not list_node:
            return True
        if not tree_node or list_node.val != tree_node.val:
            return False
        return (
                self.helper(list_node.next, tree_node.left) or
                self.helper(list_node.next, tree_node.right)
        )
