import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)  # node: list of (neighborNode, distance)
        for u, v, dist in edges:
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        # returns count of nodes reachable from src within threshold dist
        def dijkstra(src) -> int:
            minH = [(0, src)]  # (dist, node)
            visit = set()

            while minH:
                distToNode, node = heapq.heappop(minH)
                if node in visit: continue
                visit.add(node)
                for nei, dist in adj[node]:
                    nei_dist = distToNode + dist
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(minH, (nei_dist, nei))
            return len(visit) - 1  # need to discount src node

        res, min_count = -1, n  # min_count will be less than n as node can only reach n - 1 nodes
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:  # = because we need to break tie with higher node as answer
                res, min_count = src, count
        return res
