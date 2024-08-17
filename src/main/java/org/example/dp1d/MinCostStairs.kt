package org.example.dp1d

fun minCostClimbingStairs(cost: IntArray): Int {
    val cost2 = cost.toMutableList().apply { add(0) }
    for (i in (cost2.size - 3) downTo 0) {
        cost2[i] += minOf(cost2[i + 1], cost2[i + 2])
    }

    return minOf(cost2[0], cost2[1])
}

fun main() {
    val cost = intArrayOf(10, 15, 20)
    println(minCostClimbingStairs(cost))
}