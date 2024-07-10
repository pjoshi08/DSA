class Solution:
    # T: O(n), M: O(1), but fastest (90%)
    def numWaterBottles3(self, numBottles: int, numExchange: int) -> int:
        consumed = 0

        while numBottles >= numExchange:
            # Consume numExchange full bottles.
            consumed += numExchange
            numBottles -= numExchange

            # Exchange them for one full bottle.
            numBottles += 1

        return consumed + numBottles

    # T: O(log n), M: O(1)
    def numWaterBottles2(self, numBottles: int, numExchange: int) -> int:
        consumed = 0

        while numBottles >= numExchange:
            # Maximum number of times we can consume numExchange
            # number of bottles using numBottles.
            k = numBottles // numExchange

            consumed += numExchange * k
            numBottles -= numExchange * k

            numBottles += k

        return consumed + numBottles

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles < numExchange: return numBottles

        drank = 0
        full, empty = numBottles, 0
        while full > 0:
            drank += full
            empty += full

            if empty % numExchange == 0:
                full = empty // numExchange
                empty = 0
            elif empty < numExchange:
                break
            else:
                full = empty // numExchange
                empty = empty % numExchange

        return drank


obj = Solution()
print(obj.numWaterBottles(9, 3))
# print(obj.numWaterBottles(15, 4))