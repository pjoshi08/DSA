from typing import List

from org.example.tree.TreeNode import TreeNode


class Solution:
    # T: O(n ^ 2), M: O(n)
    def countPairs2(self, root: TreeNode, distance: int) -> int:
        graph, leafNodes = {}, set()
        self.createGraph(root, None, graph, leafNodes)

        count = 0
        for leaf in leafNodes:
            q = [leaf]
            seen = set()
            seen.add(leaf)

            for _ in range(distance + 1):
                # Clear all nodes with distance i
                # add nodes with distance i + 1
                size = len(q)
                for _ in range(size):
                    cur = q.pop(0)
                    if cur in leafNodes and cur != leaf:
                        count += 1
                    for nei in graph.get(cur, []):
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
        return count // 2  # because we count each leaf pair twice

    def createGraph(self, curNode, prevNode, graph, leafNodes):
        if not curNode: return

        if not curNode.left and not curNode.right:  # if curNode is leaf
            leafNodes.add(curNode)

        if prevNode:  # update graph if prevNode is not null
            if prevNode not in graph:
                graph[prevNode] = []
            graph[prevNode].append(curNode)

            if curNode not in graph:
                graph[curNode] = []
            graph[curNode].append(prevNode)

        self.createGraph(curNode.left, curNode, graph, leafNodes)
        self.createGraph(curNode.right, curNode, graph, leafNodes)

    # T: O(n * D^2), M: O(n)
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self.computeDistance(root, distance)[11]

    def computeDistance(self, node, distance) -> List[int]:
        if not node:
            return [0] * 12
        if not node.left and not node.right:  # leaf node
            current = [0] * 12
            current[0] = 1  # leaf node is distance 0 from itself
            return current

        # Leaf node count for a given distance i
        left = self.computeDistance(node.left, distance)
        right = self.computeDistance(node.right, distance)

        current = [0] * 12
        # Combine the counts from the left and right subtree and shift by
        # +1 distance
        for i in range(10):
            current[i + 1] = left[i] + right[i]

        # Initialize to total number of good leaf nodes pairs from left and right subtrees.
        current[11] = left[11] + right[11]

        # Iterate through possible leaf node distance pairs
        for d1 in range(distance + 1):
            for d2 in range(distance + 1):
                if 2 + d1 + d2 <= distance:
                    # If the total path distance is less than the given distance limit,
                    # then add to he total number of good pairs
                    current[11] += left[d1] * right[d2]

        return current

# root = [1,2,3,4,5,6,7], distance = 3, Ans = 2
