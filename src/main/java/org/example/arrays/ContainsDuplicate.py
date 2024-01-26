class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False
