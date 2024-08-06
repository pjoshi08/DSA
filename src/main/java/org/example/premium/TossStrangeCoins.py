from typing import List

# You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.
#
# Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.
# Example 1:
#
# Input: prob = [0.4], target = 1
# Output: 0.40000
# Example 2:
#
# Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# Output: 0.03125
class Solution:
    # T: O(n * target), M: O(n * target)
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        length = len(prob)
        cache = {}  # (index, heads) -> prob

        # index: 0 -> length
        # heads: 0 -> target
        def calcProb(index, heads):
            if heads > target: return 0.0  # we have already gone over target, no need to continue
            if index == length:
                if heads < target:
                    return 0.0
                return 1.0  # heads == target
            if (index, heads) in cache: return cache[(index, heads)]

            # probability of getting heads
            prob_heads = prob[index] * calcProb(index + 1, heads + 1)
            # inverse prob of getting heads i.e prob of getting tails
            prob_tails = (1 - prob[index]) * calcProb(index + 1, heads)  # we don't inc head count here
            cache[(index, heads)] = prob_heads + prob_tails
            return cache[(index, heads)]

        return calcProb(0, 0)