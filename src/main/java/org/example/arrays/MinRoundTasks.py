from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        taskFreq = Counter(tasks)

        count = 0
        for n in taskFreq.values():
            if n == 1: return -1
            count += (n // 3) + bool(n % 3)
        return count


obj = Solution()
# tasks = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
# tasks = [2,3,3]
tasks = [5, 5, 5, 5]
print(obj.minimumRounds(tasks))
