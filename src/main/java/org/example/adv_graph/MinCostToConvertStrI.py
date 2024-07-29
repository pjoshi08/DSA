import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst, curCost in zip(original, changed, cost):
            adj[src].append((dst, curCost))

        # returns a min cost map from src char to all possible/reachable dst chars
        def dijkstra(src):
            heap = [(0, src)]  # (cost, src)
            costMap = {}

            while heap:
                cost, src = heapq.heappop(heap)
                if src in costMap: continue
                costMap[src] = cost
                for nei, neiCost in adj[src]:
                    heapq.heappush(heap, (neiCost + cost, nei))
            return costMap

        # run dijkstra for every distinct char in src
        # to compute min dist from a char in src to a char in target
        minCostMaps = {c: dijkstra(c) for c in set(source)}
        cost = 0
        for src, dst in zip(source, target):
            if src == dst: continue
            if dst not in minCostMaps[src]:
                return -1
            cost += minCostMaps[src][dst]
        return cost
