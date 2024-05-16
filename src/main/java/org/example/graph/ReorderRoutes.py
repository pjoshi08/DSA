from typing import List

# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start at city 0
        # recursively check its neighbours
        # count outgoing edges
        # T = O(n), M = O(n)

        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}
        visit = set()
        changes = 0

        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal changes

            for nei in neighbors[city]:
                if nei in visit: continue
                # check if this neighbor can reach city 0
                if (nei, city) not in edges:
                    changes += 1
                visit.add(nei)
                dfs(nei)

        visit.add(0)
        dfs(0)
        return changes
