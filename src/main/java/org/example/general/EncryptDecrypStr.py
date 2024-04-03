from collections import defaultdict
from typing import List

# https://leetcode.com/problems/encrypt-and-decrypt-strings/description/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

    def search(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keyValMap = dict()
        for k, v in zip(keys, values):
            self.keyValMap[k] = v
        self.encryptions = defaultdict(int)
        for w in dictionary:
            self.encryptions[self.encrypt(w)] += 1

    def encrypt(self, word1: str) -> str:
        encrypted = []
        for c in word1:
            if c not in self.keyValMap:
                return ''
            encrypted.append(self.keyValMap[c])
        return "".join(encrypted)

    def decrypt(self, word2: str) -> int:
        return self.encryptions[word2]


# TLE solution
class Encrypter2:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.root = TrieNode()
        for w in dictionary:
            self.root.addWord(w)

    def encrypt(self, word1: str) -> str:
        encrypted = ""

        for i, s in enumerate(word1):
            if s not in self.keys: return encrypted
            index = self.keys.index(s)
            sub = self.values[index]
            encrypted += sub
        return encrypted

    def decrypt(self, word2: str) -> int:
        count = 0
        cur = self.root
        indices = []
        for i in range(0, len(word2), 2):
            indices.append(self.findValIndices(word2[i:i + 2]))

        def dfs(i, str):
            nonlocal count
            if i == len(indices):
                if cur.search(str): count += 1
                return

            for j in indices[i]:
                str += self.keys[j]
                dfs(i + 1, str)
                if j != len(indices[i]) - 1:
                    str = str[:-1]

        dfs(0, "")
        return count

    def findValIndices(self, subStr):
        indices = []
        for i, sub in enumerate(self.values):
            if sub == subStr: indices.append(i)
        return indices


# Your Encrypter object will be instantiated and called as such:
keys = ['a', 'b', 'c', 'd']
values = ["ei", "zf", "ei", "am"]
dictionary = ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]
obj = Encrypter(keys, values, dictionary)
word1 = "abcd"
word2 = "eizfeiam"
param_1 = obj.encrypt(word1)
param_2 = obj.decrypt(word2)
print(param_1)
print(param_2)
