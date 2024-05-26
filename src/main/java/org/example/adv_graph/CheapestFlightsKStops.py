import math
from collections import defaultdict
from typing import List


class Solution:
    # Bellman-Ford, 18%
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:  # s=source, d=destination, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

    # Dijkstra + Bellman-Ford, 65%, comments in method below
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        dist[src] = 0
        graph = defaultdict(list)
        for s, d, price in flights:
            graph[s].append([d, price])

        q = [[0, src, 0]]  # [price, dst, stops]
        while q:
            price, d, stops = q.pop(0)
            if stops > k: continue
            for nei, neiCost in graph[d]:
                newCost = price + neiCost
                if newCost < dist[nei] and stops <= k:
                    dist[nei] = newCost
                    q.append([newCost, nei, stops + 1])
        return -1 if dist[dst] == float('inf') else dist[dst]

    def findCheapestPrice3(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create the adjacency list to depict airports and flights in
        # the form of a graph.
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append([v, w])

        # Create a queue which stores the node and their distances from the
        # source in the form of {stops, node, dist} with ‘stops’ indicating
        # the no. of nodes between src and current node.
        q = [[0, src, 0]]

        # Distance array to store the updated distances from the source.
        dist = [math.inf] * n
        dist[src] = 0

        # Iterate through the graph using a queue like in Dijkstra with
        # popping out the element with min stops first.
        while q:
            stops, node, cost = q.pop(0)

            # We stop the process as soon as the limit for the stops reaches.
            if stops > k:
                continue
            for adjNode, edW in adj[node]:
                # We only update the queue if the new calculated dist is
                # less than the prev and the stops are also within limits.
                if cost + edW < dist[adjNode] and stops <= k:
                    dist[adjNode] = cost + edW
                    q.append([stops + 1, adjNode, cost + edW])

        # If the destination node is unreachable return ‘-1’
        # else return the calculated dist from src to dst.
        if dist[dst] == math.inf:
            return -1
        return dist[dst]
