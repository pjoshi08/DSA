from org.example.TrieNode import TrieNode


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "apple"
obj.insert(word)
param_2 = obj.search(word)
print(param_2)

prefix = "app"
print(obj.search(prefix))

param_3 = obj.startsWith(prefix)
print(param_3)
