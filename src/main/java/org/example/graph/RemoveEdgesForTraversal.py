# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.components = n

    def find(self, x: int):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # path compression
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return 0

        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.components -= 1
        return 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        remove = 0

        for t, u, v in edges:
            if t == 3:
                remove += alice.union(u, v)
                bob.union(u, v)
        for t, u, v in edges:
            if t == 1:
                remove += alice.union(u, v)
            else:
                remove += bob.union(u, v)

        if alice.components == bob.components == 1:
            return len(edges) - remove
        return -1


obj = Solution()
n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
print(obj.maxNumEdgesToRemove(n, edges))
