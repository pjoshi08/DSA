from org.example.tree.TreeNode import TreeNode


class Solution:
    # T: O(nlogn), M: O(n), bad solution
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nums = []
        def bst(node):
            if not node: return

            nums.append(node.val)
            bst(node.left)
            bst(node.right)

        def gst(node):
            if not node: return

            node.val = sumMap[node.val]
            gst(node.left)
            gst(node.right)

        bst(root)
        nums.sort(reverse=True)
        sumMap = {nums[0]: nums[0]}

        for i in range(1, len(nums)):
            total = nums[i] + nums[i - 1]
            sumMap[nums[i]] = total
            nums[i] = total

        gst(root)
        return root

    # recursive solution
    # T: O(n), M: O(n), call stack takes O(n) memory
    def bstToGst2(self, root: TreeNode) -> TreeNode:
        nodeSum = 0

        def postOrder(node):
            nonlocal nodeSum
            if not node: return

            postOrder(node.right)
            nodeSum += node.val
            node.val = nodeSum
            postOrder(node.left)

        postOrder(root)
        return root

    # iterative solution
    # T: O(n), M: O(n)
    def bstToGst2(self, root: TreeNode) -> TreeNode:
        q = []
        node = root
        nodeSum = 0

        while q or node:

            while node:
                q.append(node)
                node = node.right
            node = q.pop()

            nodeSum += node.val
            node.val = nodeSum

            node = node.left

        return root