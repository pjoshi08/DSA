class Solution:
    def twoSum(self, nums, target):
        hmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            hmap[n] = i
        return []

obj = Solution()
#nums = [3,2,4]
#nums = [2,7,11,15]
nums = [3,3]
print(obj.twoSum(nums, 6))
