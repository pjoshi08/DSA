from collections import defaultdict
from typing import List


class Solution:
    # O(n ^ 2)
    def removeStones(self, stones: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(stones)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)

        connected_components = 0
        visited = [False] * n

        def dfs(stone):
            visited[stone] = True
            for nei in adj[stone]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                connected_components += 1
        return n - connected_components

