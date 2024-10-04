class Solution:
    """
            No 2 colors should be together.
            Number of ways to paint 1 fence with k colour = k
            Number of ways to paint 2 fence with k colour = k * k (2 Adjacent fence can be same colour)
            Number of ways to paint 3 fence with k colour - there are two possibilities
            Fence 1 and Fence 2 are different colours = k * (k-1) * k
            Fence 1 and Fence 2 are same colours = k * 1 * (k - 1) - Fence 2 is set 1 once because we can
             choose only 1 colour. Fence 3 is k-1 because we cannot choose the color chosen for fence 2 and 3.

            Generalising the above step
            If f(n) is number of ways to paint n fences with k colour
            f(3) = k * (k-1) * k + k * 1 * (k -1) = (k-1) (k + k * k)
            f(3) = (k-1) (f(1) + f(2))
            This implies f(n) = (k-1) (f(n-1) +f(n-2))

            ## TIME COMPLEXITY : O(N) ##
		    ## SPACE COMPLEXITY : O(N) ##
    """

    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0: return 0
        dp = [k, k * k] + [0] * (n - 1)
        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        return dp[n - 1]
