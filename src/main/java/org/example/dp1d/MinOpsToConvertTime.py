# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/
class Solution:
    # slower
    def convertTime(self, current: str, correct: str) -> int:
        curTime = current.split(":")
        curMins = int(curTime[0]) * 60 + int(curTime[1])
        correctTime = correct.split(":")
        correctMins = int(correctTime[0]) * 60 + int(correctTime[1])
        timeDiff = correctMins - curMins

        dp = [timeDiff + 1] * (timeDiff + 1)
        dp[0] = 0
        timeOps = [1, 5, 15, 60]
        for t in range(1, timeDiff + 1):
            for op in timeOps:
                if t - op >= 0:
                    dp[t] = min(dp[t], 1 + dp[t - op])
        return dp[timeDiff]

    # beats 99%
    def convertTime2(self, current: str, correct: str) -> int:
        ops = [60, 15, 5, 1]

        def getMinutes(time) -> int:
            return int(time[:2]) * 60 + int(time[3:])

        timeDiff = getMinutes(correct) - getMinutes(current)

        res = 0
        for op in ops:
            res += timeDiff // op
            timeDiff %= op
        return res


obj = Solution()
# current = "02:30"
# correct = "04:35"
current = "11:00"
correct = "11:01"
print(obj.convertTime(current, correct))
