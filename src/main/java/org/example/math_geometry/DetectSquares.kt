package org.example.math_geometry

import kotlin.math.abs

class DetectSquares {

    private val ptsCount = mutableMapOf<Pair<Int, Int>, Int>()
    private val pts = mutableListOf<Pair<Int, Int>>()

    fun add(point: IntArray) {
        val pair = Pair(point[0], point[1])
        ptsCount[pair] = 1 + ptsCount.getOrDefault(pair, 0)
        pts.add(pair)
    }

    fun count(point: IntArray): Int {
        val (px, py) = point
        var squares = 0
        for ((x, y) in pts) {
            if (abs(px - x) != abs(py - y) || px == x || py == y)
                continue
            val p1 = Pair(px, y)
            val p2 = Pair(x, py)
            squares += ptsCount.getOrDefault(p1, 0) * ptsCount.getOrDefault(p2, 0)
        }

        return squares
    }
}