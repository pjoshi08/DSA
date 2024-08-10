package org.example.math_geometry


fun numMagicSquaresInside(grid: Array<IntArray>): Int {
    val ROWS = grid.size; val COLS = grid[0].size

    // returns 1 if square is magic else 0
    fun magic(r: Int, c: Int): Int {
        // Ensure 1-9
        val values = mutableSetOf<Int>()
        for (i in r..<r + 3) {
            for (j in c..<c + 3) {
                if (grid[i][j] in values || grid[i][j] !in 1..9) {
                    return 0
                }
                values.add(grid[i][j])
            }
        }

        // Row Sum
        for (i in r..<r + 3){
            if (grid[i].slice(c..<c + 3).sum() != 15) {
                return 0
            }
        }

        // Col Sum
        for (i in c..<c + 3) {
            if (grid[r][i] + grid[r+1][i] + grid[r+2][i] != 15) {
                return 0
            }
        }

        // Diagonal Sum
        if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 ||
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15) {
            return 0
        }

        return 1
    }

    var count = 0
    for (r in 0 until ROWS - 2) {
        for (c in 0 until COLS - 2) {
            count += magic(r, c)
        }
    }

    return count
}
