package org.example.graph;

import org.example.Pair;

import java.util.*;

public class MaxAreaIsland {
    private Set<Pair<Integer, Integer>> visited = new HashSet<>();
    private int maxArea = 0;

    private List<Pair<Integer, Integer>> directions = new ArrayList<>() {{
        add(new Pair<>(1, 0));
        add(new Pair<>(-1, 0));
        add(new Pair<>(0, 1));
        add(new Pair<>(0, -1));
    }};

    private int rows, cols;

    // T = 2ms
    public int maxAreaOfIsland(int[][] grid) {
        rows = grid.length; cols = grid[0].length;
        int maxArea = 0;

        for (int r=0; r < rows; r++)
            for (int c=0; c < cols; c++)
                if (grid[r][c] == 1)
                    maxArea = Math.max(maxArea, dfs(r, c, grid));
        return maxArea;
    }

    private int dfs(int r, int c, int[][] grid) {
        if (r < 0 || r == rows || c < 0 || c == cols || grid[r][c] == 0)
            return 0;

        // mark visited
        grid[r][c] = 0;

        int count = 1;
        count += dfs(r+1, c, grid);
        count += dfs(r-1, c, grid);
        count += dfs(r, c+1, grid);
        count += dfs(r, c-1, grid);

        return count;
    }

    // T = 10ms
    public int maxAreaOfIsland2(int[][] grid) {
        rows = grid.length; cols = grid[0].length;

        for (int r = 0; r < rows; r++)
            for(int c = 0; c < cols; c++)
                if (grid[r][c] == 1 && !visited.contains(new Pair<>(r, c)))
                    bfs(grid, r, c);

        return maxArea;
    }

    private void bfs(int[][] grid, int r, int c) {
        int area = 1;
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        q.add(new Pair<>(r, c));
        visited.add(new Pair<>(r, c));

        while (!q.isEmpty()) {
            Pair<Integer, Integer> pair = q.remove();
            int row = pair.getKey(), col = pair.getValue();

            for (Pair<Integer, Integer> dir: directions) {
                int dr = dir.getKey(), dc = dir.getValue();
                r = row + dr; c = col + dc;
                if (r >= 0 && r < rows &&
                        c >= 0 && c < cols && grid[r][c] == 1 &&
                        !visited.contains(new Pair<>(r, c))) {
                    q.add(new Pair<>(r, c));
                    visited.add(new Pair<>(r, c));
                    area += 1;
                }
            }
        }
        maxArea = Math.max(area, maxArea);
    }

    public static void main(String[] args) {
        int[][] grid = {{1,0,1}, {1,1,1}, {0,0,1}};
        System.out.println(new MaxAreaIsland().maxAreaOfIsland(grid));
    }
}

class MaxAreaIslandSolution {

    public int maxAreaOfIsland(int[][] grid) {
        int row = grid.length, col = grid[0].length;
        int maxArea = 0;
        for (int i = 0; i < row; ++i) {
            for (int j = 0; j < col; ++j) {
                if (grid[i][j] == 1) {
                    maxArea = Math.max(maxArea, dfs(grid, i, j));
                }
            }
        }

        return maxArea;
    }

    private int dfs(int[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] == 0) {
            return 0;
        }

        // visited
        grid[row][col] = 0;

        int count = 1;

        // run dfs all directions
        count += dfs(grid, row - 1, col);
        count += dfs(grid, row, col + 1);
        count += dfs(grid, row + 1, col);
        count += dfs(grid, row, col - 1);

        return count;
    }

}
