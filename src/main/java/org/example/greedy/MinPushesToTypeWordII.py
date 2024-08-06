import heapq


class Solution:
    # most freq char mapped first, as it will reduce button press count
    # array solution
    def minimumPushes(self, word: str) -> int:
        count = [0] * 26  # a ... z, also array is easier to sort
        for c in word:
            count[ord(c) - ord('a')] += 1
        count.sort(reverse=True)  # constant time, 26 chars

        res = 0
        for i, cnt in enumerate(count):
            res += cnt * (1 + i // 8)  # 8 buttons from 2-9, we batch the chars in batches of 8
        return res

    # most freq char mapped first, as it will reduce button press count
    # Heap solution
    def minimumPushes(self, word: str) -> int:
        count = [0] * 26  # a ... z, also array is easier to sort
        for c in word:
            count[ord(c) - ord('a')] -= 1  # -ve because of python maxheap

        heapq.heapify(count)

        res = 0
        i = 0
        while count:
            cnt = -heapq.heappop(count)
            res += cnt * (1 + i // 8)
            i += 1
        return res