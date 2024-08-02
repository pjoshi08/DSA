from typing import List


class Solution:
    # bottom-up dp solution, T: O(n * w), M: O(n)
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        length = len(books)
        dp = [0] * (length + 1)  # n + 1 because we want to handle the case where i == length

        for i in range(length - 1, -1, -1):
            available_width = shelfWidth
            max_height = 0
            dp[i] = float('inf')
            for j in range(i, length):
                width, height = books[j]

                if available_width < width:  # cannot fit book into curr shelf
                    break
                available_width -= width
                max_height = max(max_height, height)
                dp[i] = min(dp[i], dp[j + 1] + max_height)
        return dp[0]

    # cache solution, T: O(n * w), M: O(n)
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        length = len(books)
        cache = {}

        def calcHeight(i):
            nonlocal length
            if i == length: return 0
            if i in cache: return cache[i]

            max_height = 0
            available_width = shelfWidth
            cache[i] = float('inf')
            for j in range(i, length):
                width, height = books[j]

                if available_width < width:
                    break
                available_width -= width
                max_height = max(max_height, height)
                # calcHeight(j + 1) + max_height calculates the height at each level
                # Also, we try to minimize ith height for each iteration of j
                cache[i] = min(cache[i], calcHeight(j + 1) + max_height)

            return cache[i]

        return calcHeight(0)
