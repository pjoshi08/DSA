class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(closestSum - target):
                    closestSum = sum

                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return closestSum


obj = Solution()
nums = [-1,2,1,-4]
target = 1
# nums = [0,0,0]
# target = 1
# nums = [1,1,1,0]
# target = -100
print(obj.threeSumClosest(nums, target))
