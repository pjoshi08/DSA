from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (m + n)
        missing_sum = total_sum - sum(rolls)

        # validation
        if missing_sum > 6 * n or missing_sum < n:  # if we can't fill up n slots
            return []

        res = []
        while n:
            dice = min(6, missing_sum - n + 1)  # greedily fill slot by making sure we have enough for the rest of
            # the slots
            res.append(dice)
            missing_sum -= dice
            n -= 1
        return res
