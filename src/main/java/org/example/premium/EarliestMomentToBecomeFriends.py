from typing import List


# There are n people in a social group labeled from 0 to n - 1. You are given an array logs where
# logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.
#
# Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also,
# person a is acquainted with a person b if a is friends with b, or a is a friend of someone
# acquainted with b.
#
# Return the earliest time for which every person became acquainted with every other person.
# If there is no such earliest time, return -1.

class UnionFind:
    def __init__(self, n: int):
        # n for both parent and rank because nodes are in range [0, n - 1]
        # otherwise its n + 1
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x: int):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]  # path compression
            p = self.parent[p]
        return p

    def union(self, n1: int, n2: int):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return

        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.components -= 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()

        group = UnionFind(n)
        for t, u, v in logs:
            group.union(u, v)
            if group.components == 1:
                return t
        return -1
