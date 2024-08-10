package org.example.math_geometry

fun spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array<IntArray> {
    val directions = arrayOf(
        intArrayOf(0, 1),
        intArrayOf(1, 0),
        intArrayOf(0, -1),
        intArrayOf(-1, 0)
    )

    var r = rStart
    var c = cStart
    var i = 0
    var steps = 1
    val res = mutableListOf<IntArray>()
    var visited = 0
    val total = rows * cols
    while (visited < total) {
        repeat(2) {
            val (dr, dc) = directions[i]
            repeat(steps) {
                if (r in 0 until rows && c in 0 until cols) {
                    res.add(intArrayOf(r, c))
                    visited += 1
                }
                r += dr
                c += dc
            }
            i = (i + 1) % 4
        }
        steps += 1
    }

    return res.toTypedArray()
}