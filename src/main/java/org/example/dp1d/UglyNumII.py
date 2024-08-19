import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minH = [1]
        visit = set()
        factors = [2, 3, 5]
        for i in range(n):
            num = heapq.heappop(minH)
            if i == n - 1:
                return num

            for f in factors:
                next_num = num * f
                if next_num not in visit:
                    visit.add(next_num)
                    heapq.heappush(minH, next_num)

    # T: O(n), M: O(n)
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2, i3, i5 = 0, 0, 0

        for i in range(1, n):
            # compute min next num at each step based
            # on index and factor
            next_num = min(
                nums[i2] * 2,
                nums[i3] * 3,
                nums[i5] * 5
            )
            nums.append(next_num)
            # increase index counter for that factor
            # and handle duplicates
            if next_num == nums[i2] * 2:
                i2 += 1
            if next_num == nums[i3] * 3:
                i3 += 1
            if next_num == nums[i5] * 5:
                i5 += 1
        return nums[n - 1]
