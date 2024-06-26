package org.example.bit_manipulation;

public class SumOfTwoNumbers {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;  // calculating carry, bit shifted to the left
            a = a ^ b;
            b = tmp;  // eventually, carry becomes zero
        }
        return a;
    }
}
