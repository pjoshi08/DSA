# Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p
# and value q in the tree.
#
# The distance between two nodes is the number of edges on the path from one to the other.
class Solution:
    # dfs solution
    def findDistance(self, root, p, q):
        if p == q: return 0
        lca_node = self.find_lca(root, p, q)  # find lowest common ancestor
        return self.dfs(lca_node, p) + self.dfs(lca_node, q)  # run dfs node on both p and q and add to res

    def find_lca(self, node, p, q):
        if not node or node.val == p or node.val == q:
            return node

        left = self.find_lca(node.left, p, q)
        right = self.find_lca(node.right, p, q)

        if not left:
            return right
        elif not right:
            return left
        else:
            return node

    def dfs(self, node, target, depth=0):
        if not node: return -1
        if node.val == target: return depth

        left = self.dfs(node.left, target, depth + 1)
        if left != -1: return left  # if we were able to find in left subtree return left dist else return right

        return self.dfs(node.right, target, depth + 1)

    # BFS solution
    def findDistance2(self, root, p, q):
        lca_node = self.find_lca(root, p, q)
        bfs = [lca_node]
        dist, depth = 0, 0
        foundP, foundQ = False, False
        while bfs and not (foundP and foundQ):
            for _ in range(len(bfs)):
                node = bfs.pop(0)
                if node.val == p:
                    dist += depth
                    foundP = True
                if node.val == q:
                    dist += depth
                    foundQ = True
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)
            depth += 1
        return dist

    # Lowest common ancestor, one pass
    def findDistance3(self, root, p, q):
        if p == q: return 0
        return self.distance(root, p, q)

    def distance(self, node, p, q, depth=0):
        if not node: return 0

        # If either p or q is found, calculate the ret_distance as the maximum
        # of depth and ret_distance value for left and right subtrees.
        if node.val == p or node.val == q:
            left = self.distance(node.left, p, q, 1)
            right = self.distance(node.right, p, q, 1)

            return max(left, right) if left > 0 or right > 0 else depth

        # Otherwise, calculate the ret_distance as sum of ret_distance of left
        # and right subtree.
        left = self.distance(node.left, p, q, depth + 1)
        right = self.distance(node.right, p, q, depth + 1)
        returnDist = left + right

        # if this node is the lca, calculate return distance
        # remove the depth of lca to compute true dist b/w p and q
        if left != 0 and right != 0:
            returnDist -= 2 * depth

        return returnDist
