from typing import List

from org.example.TrieNode import TrieNode


def addWord(self, word):
    cur = self
    for c in word:
        if c not in cur.children:
            cur.children[c] = TrieNode()
        cur = cur.children[c]
    cur.endOfWord = True


TrieNode.addWord = addWord


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visit or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

    # Better, more efficient solution
    def findWords2(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = word

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, trie):
            if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    board[r][c] not in trie):
                return
            ch = board[r][c]
            cur = trie[ch]
            word = cur.pop('#', None)
            if word: res.append(word)

            board[r][c] = ''
            dfs(r + 1, c, cur)
            dfs(r - 1, c, cur)
            dfs(r, c + 1, cur)
            dfs(r, c - 1, cur)
            board[r][c] = ch

            if not cur:
                trie.pop(ch)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie)
        return res
