from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        # construct adjacency list and maintain degree of each node
        adj_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # maintain leaf nodes
        leaves = deque([i for i in range(n) if degree[i] == 1])

        # remove leaves at each iteration, and add the new leaves after updating the node degree
        # at max we can have only two MHT
        rem_nodes = n
        while rem_nodes > 2:
            leaves_count = len(leaves)
            rem_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for nei in adj_list[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)

        # the remaining leaves form the MHTs
        return list(leaves)
