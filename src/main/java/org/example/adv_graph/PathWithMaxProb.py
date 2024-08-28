import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:
        adj = defaultdict(list)  # u: [(v, prob)]
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))

        node_probs = [0.0] * n
        node_probs[start_node] = 1.0
        pq = [(-1.0, start_node)]  # maxHeap, insert -ve values because we are calculating max Prob
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end_node:
                return -cur_prob
            for next_node, next_prob in adj[cur_node]:
                if -cur_prob * next_prob > node_probs[next_node]:
                    node_probs[next_node] = -cur_prob * next_prob
                    heapq.heappush(pq, (-node_probs[next_node], next_node))
        return 0.0
