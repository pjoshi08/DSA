from typing import List


# https://leetcode.com/problems/alien-dictionary/description/
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:  # invalid dictionary
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:  # find first differing char
                    graph[w1[j]].add(w2[j])
                    break

        res = []
        visit = {}  # False = visited but not in cur path, True = visited and in path

        def dfs(c):
            if c in visit:
                return visit[c]  # cycle detected if true

            visit[c] = True  # mark true for cur path
            for nei in graph[c]:
                if dfs(nei): return True  # cycle detected
            visit[c] = False  # path completed, mark false
            res.append(c)  # post order dfs

        for c in graph:  # can traverse graph from anywhere
            if dfs(c):  # cycle detected, invalid dictionary
                return ""
        return "".join(res[::-1])
