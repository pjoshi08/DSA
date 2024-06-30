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
