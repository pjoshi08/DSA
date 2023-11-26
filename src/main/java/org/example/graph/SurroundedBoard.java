package org.example.graph;

public class SurroundedBoard {

    int rows, cols;
    public void solve(char[][] board) {
        rows = board.length; cols = board[0].length;
        // Capture border Os with Ts
        for (int r=0; r<rows; r++)
            for (int c=0; c<cols; c++)
                if (board[r][c] == 'O' &&
                        (r == 0 || r == rows-1 || c == 0 || c == cols-1))
                    capture(r, c, board);

        for (int r=0; r<rows; r++)
            for (int c=0; c<cols; c++)
                if (board[r][c] == 'O')
                    board[r][c] = 'X';

        for (int r=0; r<rows; r++)
            for (int c=0; c<cols; c++)
                if (board[r][c] == 'T')
                    board[r][c] = 'O';
    }

    private void capture(int r, int c, char[][] board) {
        if (r < 0 || r == rows || c < 0 || c == cols ||
                board[r][c] != 'O')
            return;
        board[r][c] = 'T';
        capture(r+1, c, board);
        capture(r-1, c, board);
        capture(r, c+1, board);
        capture(r, c-1, board);
    }
}
