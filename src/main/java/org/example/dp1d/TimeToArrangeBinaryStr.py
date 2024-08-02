class Solution:
    # Intuition, the problem becomes shifting 1s to the left, two cases
    # 1. If there's 1 at the ith index, it takes x steps to move 1 to the right place (x = num of 0s)
    # 2. If there's 1 at the i - 1 index, it takes x + 1 steps to move the ith 1 to the right place
    def secondsToRemoveOccurrences(self, s: str) -> int:
        steps = zeroes = 0
        for bit in s:
            if bit == '0':
                zeroes += 1
                continue
            if zeroes > 0:
                steps = max(steps + 1, zeroes)
        return steps
