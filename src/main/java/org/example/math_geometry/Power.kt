package org.example.math_geometry

import kotlin.math.abs

fun myPow(x: Double, n: Int): Double {
    fun helper(x: Double, n: Int): Double {
        if (n == 0) return 1.0
        if (x == 0.0) return 0.0

        val res = helper(x * x, n / 2)
        return if (n % 2 != 0) res * x else res
    }

    val res = helper(x, abs(n))
    return if (n < 0) 1 / res else res
}

fun main() {
    println(myPow(x = 2.00000, n = 10))
}