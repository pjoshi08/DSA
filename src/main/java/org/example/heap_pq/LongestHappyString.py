import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))

        res = []
        while pq:
            count, char = heapq.heappop(pq)

            if (len(res) >= 2 and res[-1] == char and
                    res[-2] == char):  # if two prev chars are same
                if not pq:
                    break

                tmpCount, tmpChar = heapq.heappop(pq)
                res.append(tmpChar)
                if tmpCount + 1 < 0:  # if count of this char remains after adding to res
                    heapq.heappush(pq, (tmpCount + 1, tmpChar))
                heapq.heappush(pq, (count, char))
            else:
                res.append(char)
                count += 1
                if count < 0:
                    heapq.heappush(pq, (count, char))
        return "".join(res)
