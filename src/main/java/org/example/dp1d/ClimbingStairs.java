package org.example.dp1d;

public class ClimbingStairs {
    int count=0;
    public int climbStairs(int n) {
        int one = 1, two = 1;
        for (int i=0; i < n-1; i++) {
            int temp = one;
            one = one + two;
            two = temp;
        }

        return one;

        //dfs(0, n);
        //return count;
    }

    // Bad solution, T = 2^n, exceeds time
    private void dfs(int i, int n) {
        if (i == n) {
            count += 1;
            return;
        }
        if (i > n) return;

        // Take one step
        dfs(i+1, n);

        // Take 2 steps
        dfs(i+2, n);
    }
}
