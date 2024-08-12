package org.example.graph

class RegionsCutBySlashes {
    fun regionsBySlashes(grid: Array<String>): Int {
        val ROWS = grid.size
        val COLS = grid[0].length
        val ROWS2 = 3 * ROWS
        val COLS2 = 3 * COLS
        val grid2 = Array(ROWS2) { IntArray(COLS2) { 0 } }  // 2D grid

        for (r in grid.indices) {
            for (c in grid[r].indices) {
                val r2 = 3 * r
                val c2 = 3 * c
                if (grid[r][c] == '/') {
                    // Mark Top right to bottom left
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                } else if (grid[r][c] == '\\') {
                    // Mark Top left to bottom right
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1
                }
            }
        }

        val visit = mutableSetOf<Pair<Int, Int>>()

        fun dfs(r: Int, c: Int) {
            if (r !in 0..<ROWS2 || c !in 0..<COLS2 ||
                grid2[r][c] == 1 || Pair(r, c) in visit
            )
                return

            visit.add(Pair(r, c))
            val neighbors = arrayOf(
                arrayOf(r + 1, c),
                arrayOf(r - 1, c),
                arrayOf(r, c + 1),
                arrayOf(r, c - 1)
            )

            for ((nr, nc) in neighbors) {
                dfs(nr, nc)
            }
        }


        var regions = 0
        for (r in grid2.indices) {
            for (c in grid2[r].indices) {
                if (grid2[r][c] == 0 && Pair(r, c) !in visit) {
                    dfs(r, c)
                    regions += 1
                }
            }
        }

        return regions
    }
}

fun main() {
    val obj = RegionsCutBySlashes()
    val grid = arrayOf(" /", "/ ")
    println(obj.regionsBySlashes(grid))
}
