package org.example.trie

class TrieNode{
    val children: MutableMap<Char, TrieNode> = mutableMapOf()
    var endOfWord = false
}

class Trie() {
    val root = TrieNode()

    fun insert(word: String) {
        var cur = root
        for (c in word) {
            if (!cur.children.containsKey(c)) {
                cur.children[c] = TrieNode()
            }
            cur = cur.children[c]!!
        }
        cur.endOfWord = true
    }

    fun search(word: String): Boolean {
        var cur = root
        for (c in word) {
            if (!cur.children.containsKey(c)) return false
            cur = cur.children[c]!!
        }
        return cur.endOfWord
    }

    fun startsWith(prefix: String): Boolean {
        var cur = root
        for (c in prefix) {
            if (!cur.children.containsKey(c)) return false
            cur = cur.children[c]!!
        }
        return true
    }

}