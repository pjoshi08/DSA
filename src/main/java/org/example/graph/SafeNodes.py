from typing import List


# https://leetcode.com/problems/find-eventual-safe-states/description/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i):
            if i in safe: return safe[i]
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False  # or return safe[i]
            safe[i] = True  # if we reach here that means all paths from this node are safe
            return True  # or return safe[i]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res
