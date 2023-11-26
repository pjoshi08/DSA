package org.example.graph;

import java.util.*;
import org.example.Pair;

public class NumOfIslands {

    Set<Pair<Integer, Integer>> visited = new HashSet<>();
    List<Pair<Integer, Integer>> directions = new ArrayList<Pair<Integer, Integer>>() {{
        add(new Pair<>(1, 0));
        add(new Pair<>(-1, 0));
        add(new Pair<>(0, -1));
        add(new Pair<>(0, 1));
    }};

    int rows, cols;

    public int numIslands(char[][] grid) {
        rows = grid.length; cols = grid[0].length;
        int islands = 0;

        for (int r=0; r < rows; r++)
            for (int c=0; c < cols; c++)
                if (grid[r][c] == '1') {
                    dfs(r, c, grid);
                    islands += 1;
                }
        return islands;
    }

    private void dfs(int r, int c, char[][] grid) {
        if (r < 0 || r == rows || c < 0 || c == cols || grid[r][c] == '0')
            return;

        // mark visited
        grid[r][c] = '0';
        dfs(r+1, c, grid);
        dfs(r-1, c, grid);
        dfs(r, c+1, grid);
        dfs(r, c-1, grid);
    }

    public int numIslands2(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        rows = grid.length; cols = grid[0].length;
        int islands = 0;

        for (int r=0; r < rows; r++) {
            for (int c=0; c < cols; c++)
                if (grid[r][c] == '1' && !visited.contains(new Pair<>(r, c))) {
                    bfs(grid, r, c);
                    islands += 1;
                }
        }

        return islands;
    }

    private void bfs(char[][] grid, int r, int c) {
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
                    c >= 0 && c < cols && grid[r][c] == '1' &&
                    !visited.contains(new Pair<>(r, c))) {
                    q.add(new Pair<>(r, c));
                    visited.add(new Pair<>(r, c));
                }
            }
        }
    }
}
