package org.example.dp;

public class CountBits {
    public int[] countBits(int n) {

        int[] indexNumberBitCount = new int[n+1];
        for (int i = 1; i <= n; i++) {
            int numOfBits = (int) (Math.log(i) / Math.log(2) + 1);
            int range = (int) Math.pow(2, numOfBits-1);
            indexNumberBitCount[i] = 1 + indexNumberBitCount[i - range];
        }

        return indexNumberBitCount;
    }
}
