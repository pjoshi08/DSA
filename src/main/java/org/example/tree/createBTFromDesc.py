from typing import Optional, List

from org.example.tree.TreeNode import TreeNode


class Solution:
    # descriptions[i] = [parenti, childi, isLefti]
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        nodeMap = {}  # {nodeVal: node}

        for parentVal, childVal, isLeft in descriptions:
            if parentVal not in nodeMap:
                nodeMap[parentVal] = TreeNode(parentVal)
            if childVal not in nodeMap:
                nodeMap[childVal] = TreeNode(childVal)

            if isLeft:  # isLeft == 1
                nodeMap[parentVal].left = nodeMap[childVal]
            else:
                nodeMap[parentVal].right = nodeMap[childVal]

            children.add(childVal)

        # check if node from nodeMap is not present in children
        # to find root node
        for node in nodeMap.values():
            if node.val not in children:
                return node
