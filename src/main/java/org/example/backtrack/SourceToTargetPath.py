from typing import List


# https://leetcode.com/problems/all-paths-from-source-to-target/description/
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if path[-1] == len(graph) - 1:
                res.append(path)
                return
            for node in graph[i]:
                dfs(node, path + [node])

        dfs(0, [0])
        return res


obj = Solution()
# graph = [[1,2],[3],[3],[]]
graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(obj.allPathsSourceTarget(graph))
