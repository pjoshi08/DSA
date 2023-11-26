package org.example.arrays;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import org.example.Pair;

public class ValidSudoku {

    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, Set<Character>> cols = new HashMap<>();
        HashMap<Integer, Set<Character>> rows = new HashMap<>();
        HashMap<Pair, Set<Character>> square = new HashMap<>();
        for (int r=0; r < 9; r++) {
            for (int c=0; c < 9; c++) {
                if (board[r][c] == '.') continue;

                if (rows.getOrDefault(r, new HashSet<>()).contains(board[r][c]) ||
                        cols.getOrDefault(c, new HashSet<>()).contains(board[r][c]) ||
                        square.getOrDefault(new Pair(r/3, c/3), new HashSet<>()).contains(board[r][c])) {
                    return false;
                }

                Set<Character> set = rows.getOrDefault(r, new HashSet<>());
                set.add(board[r][c]);
                rows.put(r, set);
                set = cols.getOrDefault(c, new HashSet<>());
                set.add(board[r][c]);
                cols.put(c, set);

                set = square.getOrDefault(new Pair(r/3, c/3), new HashSet<>());
                set.add(board[r][c]);
                square.put(new Pair(r/3, c/3), set);
            }
        }

        return true;
    }
}


