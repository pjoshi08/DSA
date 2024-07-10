class Solution:
    # iterative dp solution, T: O(n), M: O(1)
    # this solution arises from the recursive solution (previous submission)
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        # i starts from 2 because as in recursion, the base condition is
        # if n == 1, ans = 0
        for i in range(2, n + 1):
            res = (res + k) % i

        return res + 1

    # recursive solution, T: O(n), M: O(n)
    # In recursion, we reduce 1 player each time and shift the index by k
    # and mod it by n to keep it circular
    def findTheWinner2(self, n: int, k: int) -> int:
        def recursion(n, k):
            if n == 1: return 0
            return (recursion(n - 1, k) + k) % n

        return recursion(n, k) + 1  # add 1 to 1 indexed players

    # T: O(n^2), M: O(n)
    def findTheWinner1(self, n: int, k: int) -> int:
        circle = list(range(1, n + 1))
        start = 0
        while len(circle) > 1:
            nxt = (start + k - 1) % len(circle)  # index to remove
            circle.pop(nxt)
            start = nxt
        return circle[0]
