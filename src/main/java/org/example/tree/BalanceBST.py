from org.example.tree.TreeNode import TreeNode


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def inorder(node):
            if not node: return

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        def bst(start, end):
            if start > end: return None

            mid = start + end - start // 2
            node = TreeNode(nums[mid])
            node.left = bst(start, mid - 1)
            node.right = bst(mid + 1, end)
            return node

        inorder(root)
        return bst(0, len(nums) - 1)