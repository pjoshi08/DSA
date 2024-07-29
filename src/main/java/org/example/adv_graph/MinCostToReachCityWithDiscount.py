import heapq
from collections import defaultdict
from typing import List


# A series of highways connect n cities numbered from 0 to n - 1. You are given a 2D integer array highways where
# highways[i] = [city1i, city2i, tolli] indicates that there is a highway that connects city1i and city2i, allowing
# a car to go from city1i to city2i and vice versa for a cost of tolli.
#
# You are also given an integer discounts which represents the number of discounts you have. You can use a discount
# to travel across the ith highway for a cost of tolli / 2 (integer division). Each discount may only be used once,
# and you can only use at most one discount per highway.
#
# Return the minimum total cost to go from city 0 to city n - 1, or -1 if it is not possible to go from city 0 to
# city n - 1.
class Solution:
    def minimumCost2(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, toll in highways:
            adj[u].append((v, toll))
            adj[v].append((u, toll))

        minH = [(0, 0, 0)]  # (curCityCost, city, discountsUsed)
        # array to calc cost to reach city based on num of discounts used
        dist = [[float('inf')] * (discounts + 1) for _ in range(n)]

        while minH:
            curCost, city, discountsUsed = heapq.heappop(minH)

            # If we cannot improve from this city, don't continue
            if curCost > dist[city][discountsUsed]: continue

            for nei, toll in adj[city]:
                # Case 1: proceed to next city without using discount if dist is less than existing
                newCost = curCost + toll
                if newCost < dist[nei][discountsUsed]:
                    dist[nei][discountsUsed] = newCost
                    heapq.heappush(minH, (newCost, nei, discountsUsed))

                # Case 2: proceed to next city using a discount
                if discountsUsed < discounts:
                    newCost = curCost + toll // 2
                    if newCost < dist[nei][discountsUsed + 1]:
                        dist[nei][discountsUsed + 1] = newCost
                        heapq.heappush(minH, (newCost, nei, discountsUsed + 1))

        minCost = min(dist[n - 1])
        return minCost if minCost != float('inf') else -1

    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        adj = defaultdict(list)
        for u, v, toll in highways:
            adj[u].append((v, toll))
            adj[v].append((u, toll))

        minH = [(0, 0, 0)]  # minHeap to store distance to curr city, cur city, discounts used
        # array to calc cost to reach city based on num of discounts used
        dist = [[float('inf')] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0

        # keep track of visited nodes based on num of discounts used
        visit = [[False] * (discounts + 1) for _ in range(n)]

        while minH:
            curCost, city, discountsUsed = heapq.heappop(minH)

            if visit[city][discountsUsed]: continue
            visit[city][discountsUsed] = True  # else mark cur city as visited based on num of discounts

            for nei, toll in adj[city]:
                # Case 1: proceed to next city without using discount if dist is less than existing
                newCost = curCost + toll
                if newCost < dist[city][discountsUsed]:
                    dist[city][discountsUsed] = newCost
                    heapq.heappush(minH, (newCost, nei, discountsUsed))

                # Case 2: proceed to next city using a discount
                if discountsUsed < discounts:
                    newCost = curCost + toll // 2
                    if newCost < dist[city][discountsUsed + 1]:
                        dist[city][discountsUsed + 1] = newCost
                        heapq.heappush(minH, (newCost, nei, discountsUsed + 1))

        minCost = min(dist[n - 1])
        return minCost if minCost != float('inf') else -1
