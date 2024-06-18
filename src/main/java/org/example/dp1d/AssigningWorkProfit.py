from typing import List


# https://leetcode.com/problems/most-profit-assigning-work/?envType=daily-question&envId=2024-06-18
class Solution:
    # Memoization solution, O(n + m + maxAbility) but leetcode 7.54%
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)

        # calculate profit for a job
        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])

        # calculate max profit that can be done for a job
        for i in range(1, maxAbility + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])

        profit = 0
        # calculate profit
        for ability in worker:
            profit += jobs[ability]
        return profit

    # Solution 1: O(nlogn + mlogm) but leetcode: 39%
    def maxProfitAssignment1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # jobs = [(difficulty[i], profit[i]) for i in range(len(difficulty))]
        # jobs.sort()
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        i, maxProfit, netProfit = 0, 0, 0
        for ability in worker:
            # Check if the worker can do the work
            # increase index till he can maximize profit
            while i < len(difficulty) and ability >= jobs[i][0]:
                maxProfit = max(maxProfit, jobs[i][1])
                i += 1
            netProfit += maxProfit
        return netProfit
