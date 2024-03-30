from typing import List


# https://leetcode.com/problems/replace-words/description/
class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res = []

        for word in dictionary:
            self.insert(word)

        sentence = sentence.split()
        for word in sentence:
            root = self.getRoot(word)
            if root:
                res.append(root)
            else:
                res.append(word)

        return " ".join(res)

    def getRoot(self, word):
        cur = self.root
        root = ''
        for c in word:
            if c not in cur.children or cur.endOfWord:
                break
            root += c
            cur = cur.children[c]

        return root if cur.endOfWord else ''

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True


obj = Solution()
# dictionary = ["cat", "bat", "rat"]
dictionary = ["a", "aa", "aaa", "aaaa"]
# sentence = "the cattle was rattled by the battery"
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(obj.replaceWords(dictionary, sentence))
