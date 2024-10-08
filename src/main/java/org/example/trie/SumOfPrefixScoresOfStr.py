from collections import defaultdict
from typing import List


class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, w):
        cur = self.root
        for c in w:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = PrefixNode()
            cur = cur.children[i]
            cur.count += 1

    def get_score(self, w) -> int:
        cur = self.root
        score = 0
        for c in w:
            i = ord(c) - ord('a')
            cur = cur.children[i]
            score += cur.count
        return score


class Solution:
    # T: O(n * l) solution
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        prefix_tree = PrefixTree()
        for w in words:
            prefix_tree.insert(w)

        for w in words:
            res.append(prefix_tree.get_score(w))

        return res

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        count = defaultdict(int)

        # O(n * l * l)
        for w in words:
            for i in range(len(w)):
                count[w[:i + 1]] += 1

        for w in words:
            score = 0
            for i in range(len(w)):
                score += count[w[:i + 1]]
            res.append(score)
        return res
