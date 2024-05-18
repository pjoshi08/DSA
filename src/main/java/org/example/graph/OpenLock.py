from collections import deque
from typing import List


# https://leetcode.com/problems/open-the-lock/description/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set(deadends)
        if '0000' in visit or target in visit: return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        q = deque()  # [lock, turns]
        q.append(['0000', 0])
        while q:
            lock, turns = q.popleft()
            if lock == target: return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])
        return -1
