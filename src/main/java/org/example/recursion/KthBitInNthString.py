class Solution:
    # Iterative Solution, better memory complexity
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        invert = False

        while length > 1:
            half = length // 2

            if k <= half:
                length = half
            elif k > half + 1:
                k = 1 + length - k
                length = half
                invert = not invert
            else:
                return "1" if not invert else "0"
        return "0" if not invert else "1"

    # Recursive solution, T: O(n), M: O(n)
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1
        invert = False

        def helper(length, k, invert):
            if length == 1:  # n == 1, len == 1
                return "0" if not invert else "1"

            half = length // 2
            # len = 15, half = 7
            if k <= half:
                return helper(half, k, invert)
            elif k > half + 1:  # +1 because mid will always be 1
                return helper(half, 1 + length - k, not invert)
            else:
                return "1" if not invert else "0"

        return helper(length, k, invert)

    # Recursive solution, T: O(n), M: O(n)
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1

        def helper(length, k):
            if length == 1: return "0"  # n == 1, len == 1

            half = length // 2
            # len = 15, half = 7
            if k <= half:
                return helper(half, k)
            elif k > half + 1:  # +1 because mid will always be 1
                res = helper(half, 1 + length - k)
                return "0" if res == "1" else "1"
            else:
                return "1"

        return helper(length, k)
