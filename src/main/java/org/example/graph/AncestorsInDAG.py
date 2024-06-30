from typing import List

# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]
        topological_sort = []

        while nodes_with_zero_indegree:
            node = nodes_with_zero_indegree.pop(0)
            topological_sort.append(node)

            # for all the neighbors for cur node, reduce indegree
            # and add those nodes whose indgree becomes zero
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    nodes_with_zero_indegree.append(nei)

        ancestors = [set() for _ in range(n)]
        res = [[] for _ in range(n)]

        for node in topological_sort:
            for nei in graph[node]:
                # first add the immediate parent, then other ancestors
                ancestors[nei].add(node)
                ancestors[nei].update(ancestors[node])

        for i in range(n):
            res[i].extend(ancestors[i])
            res[i].sort()
        return res


obj = Solution()
n = 8
edgeList = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
print(obj.getAncestors(n, edgeList))
