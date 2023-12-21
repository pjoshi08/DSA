class Solution(object):
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # new interval is overlapping in this case
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res


solution = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(solution.insert(intervals, newInterval))
