import collections
from typing import List


# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/submissions/1239112749/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visit = set()
        graph = collections.defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        def dfs(n):
            if n in visit: return
            visit.add(n)
            for node in graph[n]:
                dfs(node)

        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1
        return count


obj = Solution()
# n = 5
# edges = [[0, 1], [1, 2], [3, 4]]
n = 3
edges = [[1,0]]
print(obj.countComponents(n, edges))
