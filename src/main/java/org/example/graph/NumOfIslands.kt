package org.example.graph


fun numIslands(grid: Array<CharArray>): Int {
    val ROWS = grid.size
    val COLS = grid[0].size

    val visit = mutableSetOf<Pair<Int, Int>>()
    val dirs = listOf(
        intArrayOf(1, 0),
        intArrayOf(-1, 0),
        intArrayOf(0, 1),
        intArrayOf(0, -1)
    )

    fun dfs(r: Int, c: Int) {
        if (r < 0 || r == ROWS || c < 0 || c == COLS ||
            (r to c) in visit || grid[r][c] == '0') {
            return
        }

        visit.add((r to c))
        for ((dr, dc) in dirs) {
            dfs(r + dr, c + dc)
        }
    }

    var count = 0
    for (r in 0 until ROWS) {
        for (c in 0 until COLS) {
            if ((r to c) !in visit && grid[r][c] == '1') {
                dfs(r, c)
                count++
            }
        }
    }

    return count
}

fun main() {
    val grid = arrayOf(
        charArrayOf('1', '1', '0', '0', '0'),
        charArrayOf('1', '1', '0', '0', '0'),
        charArrayOf('0', '0', '1', '0', '0'),
        charArrayOf('0', '0', '0', '1', '1')
    )
    println(numIslands(grid))
}