from collections import defaultdict, deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([1])  # nodes 1 to n
        res = -1
        cur_time = 0
        visit_times = defaultdict(list)  # node -> [visit times], to store 2nd best time
        # this list only stores at max 2 values

        while q:  # normal bfs
            for _ in range(len(q)):
                node = q.popleft()
                if node == n:
                    if res != -1:  # if this is the 2nd best time
                        return cur_time
                    res = cur_time  # else mark the best time, and proceed to find 2nd best time
                for nei in adj[node]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        visit_times[nei].append(cur_time)
                        q.append(nei)

            if (cur_time // change) % 2 == 1:  # if we are at red light, increase time till green light
                # green light happens at even intervals
                # (cur_time % change) + X = change
                # X = change - (cur_time % change)
                cur_time += change - (cur_time % change)
            # now increase cur_time since we are at green light time
            cur_time += time
