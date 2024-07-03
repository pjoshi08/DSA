# Given the root of a binary search tree (BST) and an integer target, split the tree into two
# subtrees where the first subtree has nodes that are all smaller or equal to the target value,
# while the second subtree has all nodes that are greater than the target value. It is not
# necessarily the case that the tree contains a node with the value target.
#
# Additionally, most of the structure of the original tree should remain. Formally, for any
# child c with parent p in the original tree, if they are both in the same subtree after the
# split, then node c should still have the parent p.
#
# Return an array of the two roots of the two subtrees in order.
from typing import Optional, List

from org.example.tree.TreeNode import TreeNode


class Solution:
    # T: O(h), M: O(h), recursive
    def splitBST3(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root: return [None, None]

        # if root val is greater than target
        # recursively split the left subtree
        if root.val > target:
            left = self.splitBST3(root.left, target)
            # attach right part of the split to root's left subtree
            root.left = left[1]
            return [left[0], root]
        else:  # otherwise recursively split the right subtree
            right = self.splitBST3(root.right, target)
            # attach left part of the split to root's right subtree
            root.right = right[0]
            return [root, right[1]]

    # T: O(h), M: O(h), iterative, fastest
    def splitBST2(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        # ans[0] contains nodes less than target, ans[0] > target
        ans = [None, None]

        if not root: return ans
        # Stack to traverse the tree and find the split point
        stack = []
        # find nodes closest to the target
        while root:
            stack.append(root)
            if root.val > target:
                root = root.left
            else:
                root = root.right
        # Process nodes in reverse order from the stack to perform the split
        while stack:
            cur = stack.pop()
            if cur.val > target:
                # Assign cur node's left child to the subtree
                # containing nodes greater than target
                cur.left = ans[1]
                # cur node becomes new root of this subtree
                ans[1] = cur
            else:
                # assign cur node's right child to the subtree
                # with nodes less than or eq to target
                cur.right = ans[0]
                # cur node becomes root of this subtree
                ans[0] = cur
        return ans

    # T: O(n), M: O(1)
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        dummy_sm = TreeNode(0)
        cur_sm = dummy_sm
        dummy_lg = TreeNode(0)
        cur_lg = dummy_lg

        cur = root
        next_node = None

        while cur:
            if cur.val <= target:
                # link to the smaller tree node
                cur_sm.right = cur
                # move to the next node
                cur_sm = cur

                # save the next node
                # we move to the right because the next right node
                # might be larger than the target
                next_node = cur.right

                # sever the existing link
                cur.right = None

                # move to the next node
                cur = next_node
            else:  # cur.val > target
                # link to the larger tree node
                cur_lg.left = cur
                cur_lg = cur  # move to the next node

                # save the next node
                # we move to the left because the next left node
                # might be smaller or eq to the target
                next_node = cur.left

                # sever the existing link
                cur.left = None

                # move to the next node
                cur = next_node
        return [dummy_sm.right, dummy_lg.left]
