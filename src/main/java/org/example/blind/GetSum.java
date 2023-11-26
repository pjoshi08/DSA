package org.example.blind;

public class GetSum {
    // without using `+` or `-` operators
    public int getSum(int a, int b) {

        while (b != 0) {
            int temp = (a & b) << 1;
            a = a ^ b;
            b = temp;
        }

        return a;
    }
}
