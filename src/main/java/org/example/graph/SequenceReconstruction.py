import collections
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        values = {x for seq in sequences for x in seq}
        graph = {x: [] for x in values}
        degree = {x: 0 for x in values}
        # construct graph and calculate in-degree for each node
        for seq in sequences:
            for i in range(len(seq) - 1):
                s = seq[i]
                t = seq[i + 1]
                graph[s].append(t)
                degree[t] += 1

        q = collections.deque()
        # find the root node
        for node, count in degree.items():
            if count == 0:
                q.append(node)
        res = []
        # removes root in each iteration and decrease the in-degree for each node
        # if in-degree becomes 0, then that node becomes root
        while q:
            if len(q) != 1: return False
            source = q.popleft()
            res.append(source)
            for target in graph[source]:
                degree[target] -= 1
                if degree[target] == 0:
                    q.append(target)
        # check if the output is equal to both the values in sequences and nums for shortest supersequence
        return len(res) == len(values) and nums == res

obj = Solution()
nums = [1,2,3]
sequences = [[1,2],[1,3],[2,3]]
print(obj.sequenceReconstruction(nums, sequences))