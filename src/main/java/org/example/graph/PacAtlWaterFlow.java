package org.example.graph;

import org.example.Pair;

import java.util.*;
import java.util.AbstractList;

public class PacAtlWaterFlow {

    List<List<Integer>> res = new ArrayList<>();
    private Set<Pair<Integer, Integer>> pac = new HashSet<>();
    private Set<Pair<Integer, Integer>> atl = new HashSet<>();
    int rows, cols;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        rows = heights.length; cols = heights[0].length;

        for (int c=0; c < cols; c++)
            //pacificDfs(0, c, heights[0][c], heights);
            pacificDfs(0, c, 0, heights);
        for (int r=0; r < rows; r++)
            //pacificDfs(r, 0, heights[r][0], heights);
            pacificDfs(r, 0, 0, heights);


        for (int c=0; c < cols; c++)
            //atlanticDfs(rows-1, c, heights[rows-1][c], heights);
            atlanticDfs(rows-1, c, 0, heights);
        for (int r=0; r < rows; r++)
            //atlanticDfs(r, cols-1, heights[r][cols-1], heights);
            atlanticDfs(r, cols-1, 0, heights);

        return res;
    }

    private void pacificDfs(int r, int c, int prevHeight, int[][] heights) {
        if (r < 0 || r == rows || c < 0 || c == cols || heights[r][c] >= 100_001 ||
                heights[r][c] < prevHeight) return;
        //if (r < 0 || r == rows || c < 0 || c == cols) return;
        int height = heights[r][c];
        //if (height >= 100_001) return;
        //if (height < prevHeight) return;

        heights[r][c] = height + 100_001;
        pacificDfs(r+1, c, height, heights);
        pacificDfs(r-1, c, height, heights);
        pacificDfs(r, c+1, height, heights);
        pacificDfs(r, c-1, height, heights);
    }

    private void atlanticDfs(int r, int c, int prevHeight, int[][] heights) {
        if (r < 0 || r == rows || c < 0 || c == cols || heights[r][c] == -1) return;

        int height = heights[r][c];
        if (height >= 100_001) {
            height -= 100_001;
            if (height < prevHeight) return;

            res.add(Arrays.asList(r, c));
        }

        if (height < prevHeight) return;

        heights[r][c] = -1;

        atlanticDfs(r+1, c, height, heights);
        atlanticDfs(r-1, c, height, heights);
        atlanticDfs(r, c+1, height, heights);
        atlanticDfs(r, c-1, height, heights);
    }

    public List<List<Integer>> pacificAtlantic2(int[][] heights) {
        rows = heights.length; cols = heights[0].length;

        for (int c=0; c < cols; c++) {
            dfs(0, c, pac, heights[0][c], heights);
            dfs(rows-1, c, atl, heights[rows-1][c], heights);
        }

        for (int r=0; r < rows; r++) {
            dfs(r, 0, pac, heights[r][0], heights);
            dfs(r, cols-1, atl, heights[r][cols-1], heights);
        }

        for (int r=0; r < rows; r++)
            for (int c=0; c < cols; c++) {
                Pair<Integer, Integer> pos = new Pair<>(r, c);
                if (pac.contains(pos) && atl.contains(pos)) {
                    List<Integer> list = new ArrayList<>() {{
                        add(pos.getKey());
                        add(pos.getValue());
                    }};
                    res.add(list);
                }
            }

        return res;
    }

    private void dfs(int r, int c, Set<Pair<Integer, Integer>> visit, int prevHeight,
                     int[][] heights) {
        Pair<Integer, Integer> pos = new Pair<>(r, c);
        if (visit.contains(pos) || r < 0 || r == rows || c < 0 || c == cols ||
            heights[r][c] < prevHeight) return;
        visit.add(pos);
        dfs(r+1, c, visit, heights[r][c], heights);
        dfs(r-1, c, visit, heights[r][c], heights);
        dfs(r, c+1, visit, heights[r][c], heights);
        dfs(r, c-1, visit, heights[r][c], heights);
    }

    public static void main(String[] args) {
        int[][] heights = {{1,2,2,3,5}, {3,2,3,4,4}, {2,4,5,3,1}, {6,7,1,4,5}, {5,1,1,2,4}};
        //int[][] heights = {{1}};
        System.out.println(new PacAtlWaterFlow().pacificAtlantic(heights));
    }
}

class Solution {
    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        // from the pacific

        // columns
        for (int j = 0; j < heights[0].length; j++) {
            dfsFromPacific(heights, 0, 0, j);
        }

        // rows
        for (int i = 1; i < heights.length; i++) {
            Set<String> visited = new HashSet<>();
            dfsFromPacific(heights, 0, i, 0);
        }

        // from the atlantic

        // columns
        for (int j = 0; j < heights[0].length; j++) {
            dfsFromAtlantic(heights, 0, heights.length - 1, j);
        }

        // rows
        for (int i = 0; i < heights.length; i++) {
            dfsFromAtlantic(heights, 0, i, heights[0].length - 1);
        }

        return result;
    }

    private void dfsFromPacific(int[][] heights, int prevHeight, int i, int j) {
        if (i < 0 || i == heights.length || j < 0 || j == heights[0].length) {
            return;
        }

        int height = heights[i][j];

        if (height >= 100_001) {
            return;
        }

        if (height < prevHeight) {
            return;
        }

        heights[i][j] = height + 100_001;
        //System.out.println(i+"-"+j);

        dfsFromPacific(heights, height, i - 1, j); // up
        dfsFromPacific(heights, height, i + 1, j); // down
        dfsFromPacific(heights, height, i, j - 1); // left
        dfsFromPacific(heights, height, i, j + 1); // right
    }

    private void dfsFromAtlantic(int[][] heights, int prevHeight, int i, int j) {
        if (i < 0 || i == heights.length || j < 0 || j == heights[0].length) {
            return;
        }

        int height = heights[i][j];

        if (height == -1) {
            return;
        }

        if (height >= 100_001) {
            height -= 100_001;
            if (height < prevHeight) {
                return;
            }

            result.add(Arrays.asList(i, j));
        }

        if (height < prevHeight) {
            return;
        }

        heights[i][j] = -1;

        dfsFromAtlantic(heights, height, i - 1, j); // up
        dfsFromAtlantic(heights, height, i + 1, j); // down
        dfsFromAtlantic(heights, height, i, j - 1); // left
        dfsFromAtlantic(heights, height, i, j + 1); // right
    }
}