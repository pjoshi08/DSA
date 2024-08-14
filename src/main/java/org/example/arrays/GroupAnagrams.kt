package org.example.arrays

fun groupAnagrams(strs: Array<String>): List<List<String>> {
    val hashMap = HashMap<List<Int>, ArrayList<String>>()

    for (str in strs) {
        val count = MutableList(26) { 0 }
        for (c in str) {
            //val charInt = c - 'a'
            count[c - 'a'] += 1
        }
        if (count !in hashMap) {
            hashMap[count] = ArrayList()
        }
        hashMap[count]!!.add(str)
    }

    return hashMap.values.toList()
}

