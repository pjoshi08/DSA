from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to the list of its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # a set to track the nodes visited in the current dfs path
        visit = set()

        def dfs(crs):
            if crs in visit: return False
            if not preMap[crs]: return True

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visit.remove(crs)
            preMap[crs] = []

            return True

        # we run dfs for each node in case the prereq graph is disjointed
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
