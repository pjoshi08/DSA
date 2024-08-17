package org.example.binarysearch

import kotlin.math.ceil

fun minEatingSpeed(piles: IntArray, h: Int): Int {
    var l = piles.sum() / h
    var r = piles.maxOrNull()!!

    while (l < r) {
        val m = l + (r - l) / 2
        var hours = 0.0
        for (p in piles) {
            hours += ceil(p.toDouble() / m)
        }

        if (hours <= h) {
            r = m
        } else {
            l = m + 1
        }
    }
    return l
}

fun main() {
    val piles = intArrayOf(3,6,7,11)
    val h = 8
    println(minEatingSpeed(piles, h))
}