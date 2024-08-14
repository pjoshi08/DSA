package org.example.arrays

class Codec {
    // Encodes a list of strings to a single string.
    fun encode(strs: List<String>): String {
        var res = ""
        for (word in strs) {
            res += "${word.length}#${word}"
        }
        return res
    }

    // Decodes a single string to a list of strings.
    fun decode(s: String): List<String> {
        val res = mutableListOf<String>()
        var i = 0
        var j = 0
        while (i < s.length) {
            while (s[i] != '#') {
                i++
            }
            val length = s.substring(j, i).toInt()  // i points to #, don't include
            val end = i + length + 1
            res.add(s.substring(i + 1, end))
            i += length + 1
            j = i
        }
        return res
    }
}