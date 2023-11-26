package org.example.graph;

import org.example.Pair;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class RottenOranges {

    List<Pair<Integer, Integer>> directions = new ArrayList<Pair<Integer, Integer>>() {{
        add(new Pair<>(1, 0));
        add(new Pair<>(-1, 0));
        add(new Pair<>(0, -1));
        add(new Pair<>(0, 1));
    }};
    public int orangesRotting(int[][] grid) {
        Queue<Pair<Integer, Integer>> q = new LinkedList<>();
        int time=0, fresh = 0;
        int rows = grid.length, cols = grid[0].length;

        for (int r=0; r<rows; r++)
            for (int c=0; c<cols; c++) {
                if (grid[r][c] == 1) fresh += 1;
                if (grid[r][c] == 2) q.add(new Pair<>(r, c));
            }

        while (!q.isEmpty() && fresh > 0) {

            int size = q.size();
            for (int i=0; i < size; i++) {
                Pair<Integer, Integer> pos = q.remove();
                int r = pos.getKey(), c = pos.getValue();

                for (Pair<Integer, Integer> dir: directions) {
                    int row = r + dir.getKey(), col = c + dir.getValue();
                    if (row < 0 || row == rows || col < 0 || col == cols ||
                    grid[row][col] != 1) continue;

                    grid[row][col] = 2;
                    q.add(new Pair<>(row, col));
                    fresh -= 1;
                }
            }
            time += 1;
        }

        if (fresh == 0) return time;
        return -1;
    }
}
