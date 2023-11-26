package org.example.dp;

public class Tribonacci {

    public int tribonacci(int n) { // 0 <= n <= 37
        int Tn = 0;
        if (n == 0) return Tn;
        int Tn1 = 1;
        if (n == 1) return Tn1;
        int Tn2 = 1;
        if (n == 2) return Tn2;
        int trib = 0;
        for (int i = 3; i < n+1; i++) {
            trib = Tn + Tn1 + Tn2; // Tn+3 = Tn + Tn+1 + Tn+2
            Tn = Tn1;
            Tn1 = Tn2;
            Tn2 = trib;
        }

        return trib;
    }
}
