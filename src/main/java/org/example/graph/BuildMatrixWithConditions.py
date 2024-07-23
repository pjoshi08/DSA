from collections import defaultdict
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def dfs(src, adj, visit, path, order):
            if src in path:  # cycle detected
                return False
            if src in visit:
                return True
            path.add(src)
            visit.add(src)
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            order.append(src)
            path.remove(src)
            return True

        def topo_sort(conditions):
            adj = defaultdict(list)
            for src, dst in conditions:
                adj[src].append(dst)
            visit, path = set(), set()
            order = []
            for src in range(1, k + 1):  # run topo sort 1 to k as nodes can be disjointed
                if not dfs(src, adj, visit, path, order):
                    return []
            return order[::-1]  # reverse

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)
        if not row_order or not col_order: return []

        val_to_row = {n: i for i, n in enumerate(row_order)}
        val_to_col = {n: i for i, n in enumerate(col_order)}
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            matrix[r][c] = num
        return matrix
