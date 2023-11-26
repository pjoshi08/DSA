package org.example.backtrack;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class NQueens {

    List<List<String>> res = new ArrayList<>();
    Set<Integer> cols = new HashSet<>();
    Set<Integer> posDiag = new HashSet<>();
    Set<Integer> negDiag = new HashSet<>();
    List<String> board = new ArrayList<>();
    public List<List<String>> solveNQueens(int n) {

        for (int i = 0; i < n; i++) {
            StringBuilder builder = new StringBuilder();
            for (int j = 0; j < n; j++)
                builder.append(".");
            board.add(builder.toString());
        }

        backtrack(0, n);
        return res;
    }

    private void backtrack(int r, int n) {
        if (r == n) {
            res.add(new ArrayList<>(board));
            return;
        }

        for (int c=0; c < n; c++) {
            if (cols.contains(c) || posDiag.contains((r + c)) || negDiag.contains(r - c))
                continue;

            cols.add(c);
            posDiag.add(r + c);
            negDiag.add(r - c);
            StringBuilder builder = new StringBuilder(board.get(r));
            builder.setCharAt(c, 'Q');
            board.set(r, builder.toString());

            backtrack(r + 1, n);

            cols.remove(c);
            posDiag.remove(r + c);
            negDiag.remove(r - c);
            builder = new StringBuilder(board.get(r));
            builder.setCharAt(c, '.');
            board.set(r, builder.toString());
        }
    }

    public static void main(String[] args) {
        System.out.println(new NQueens().solveNQueens(4));
    }
}

class NQSolution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> ans = new ArrayList<>();
        boolean[][] board = new boolean[n][n];
        queen(ans, board, 0, n);
        return ans;
    }

    public void queen(List<List<String>> ans, boolean[][] board, int row, int n) {
        if(row == n) {
            List<String> temp = new ArrayList<>();
            create(temp, board);
            ans.add(temp);
            return;
        }
        for(int col = 0; col < n; col++) {
            if(isSafe(board, row, col)) {
                board[row][col] = true;
                queen(ans, board, row + 1, n);
                board[row][col] = false;
            }
        }
    }

    public boolean isSafe(boolean[][] board, int row, int col) {
        for(int i = 0; i < row; i++) {
            if(board[i][col])
                return false;
        }

        int maxLeft = Math.min(row, col);
        for(int i = 1; i <= maxLeft; i++) {
            if(board[row - i][col - i])
                return false;
        }

        int maxRight = Math.min(row, board.length - 1 - col);
        for(int i = 1; i <= maxRight; i++) {
            if(board[row - i][col + i])
                return false;
        }

        return true;
    }

    public void create(List<String> temp, boolean[][] board) {
        for(int i = 0; i < board.length; i++) {
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < board[0].length; j++) {
                if(board[i][j])
                    sb.append('Q');
                else
                    sb.append('.');
            }
            temp.add(sb.toString());
        }
    }
}
