import collections

from org.example.tree.TreeNode import TreeNode


class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


obj = Codec()
n4 = TreeNode(4)
n5 = TreeNode(5)
n3 = TreeNode(3, n4, n5)
n2 = TreeNode(2)
n1 = TreeNode(1, n2, n3)
data = obj.serialize(n1)
print(data)
print(obj.deserialize(data))
