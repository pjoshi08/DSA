from collections import defaultdict
from typing import List

# https://leetcode.com/problems/graph-valid-tree/description/?source=submission-ac
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1: return True
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visit = set()

        def dfs(u, prev):
            if u in visit: return False

            visit.add(u)
            for v in adj_list[u]:
                if v == prev: continue
                if not dfs(v, u): return False
            return True

        return dfs(0, -1) and n == len(visit)


obj = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
print(obj.validTree(n, edges))
