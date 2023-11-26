package org.example.backtrack;

import org.apache.commons.lang3.tuple.Pair;

import java.util.HashSet;
import java.util.Set;

public class WordSearch {

    private int ROWS, COLS;
    private Set<Pair<Integer, Integer>> path = new HashSet<>();

    public boolean exist(char[][] board, String word) {
        ROWS = board.length;
        COLS = board[0].length;

        for (int r=0; r < ROWS; r++) {
            for (int c=0; c < COLS; c++) {
                if (dfs(r, c, 0, board, word)) return true;
            }
        }

        return false;
    }

    private boolean dfs(int r, int c, int i, char[][] board, String word) {
        if (i == word.length()) return true;

        if (r < 0 || c < 0 || r >= ROWS || c >= COLS ||
                path.contains(Pair.of(r, c)) ||
                word.charAt(i) != board[r][c]
        ) return false;

        Pair<Integer, Integer> pair = Pair.of(r, c);
        path.add(pair);
        boolean res = (dfs(r+1, c, i+1, board, word) ||
                dfs(r-1, c, i+1, board, word) ||
                dfs(r, c+1, i+1, board, word) ||
                dfs(r, c-1, i+1, board, word)
        );
        path.remove(pair);
        return res;
    }
}

class Solution {
    boolean vis[][];
    public boolean exist(char[][] board, String word) {
        char ch=word.charAt(0);
        vis=new boolean [board.length][board[0].length];
        for(int i=0;i<board.length;i++)
        {
            for(int j=0;j<board[0].length;j++)
            {
                if(board[i][j]==word.charAt(0)&&dfs(i,j,0,board,word))
                    return true;
            }
        }
        return false;
    }
    public boolean dfs(int i,int j,int k,char[][]board,String word)
    {
        if(k==word.length())
            return true;
        if(i<0||i>=board.length||j<0||j>=board[0].length||board[i][j]!=word.charAt(k)||vis[i][j])
            return false;
        vis[i][j]=true;
        boolean ans=   dfs(i+1,j,k+1,board,word)|| dfs(i-1,j,k+1,board,word)||dfs(i,j-1,k+1,board,word)||dfs(i,j+1,k+1,board,word);
        vis[i][j]=false;
        return ans;
    }
}
