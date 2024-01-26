from org.example.tree.TreeNode import TreeNode


class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if not p and not q: return True

        if not p: return False
        if not q: return False

        subLeft = (p.val == q.val) and self.isSameTree(p.left, q.left)
        subRight = (p.val == q.val) and self.isSameTree(p.right, q.right)
        return subLeft and subRight
