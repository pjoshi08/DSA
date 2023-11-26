package org.example.blind;

public class ClimbingStairs {
    public int climbStairs(int n) {
        int one = 1, two = 1, temp;

        for (int i = 0; i < n-1; i++) {
            temp = one;
            one = one + two;
            two = temp;
        }

        return one;
    }
}
