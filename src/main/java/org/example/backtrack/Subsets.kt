package org.example.backtrack

fun subsets(nums: IntArray): List<List<Int>> {
    val res = mutableListOf<List<Int>>()
    val sub = mutableListOf<Int>()
    val n = nums.size

    fun backtrack(i: Int) {
        if (i == n) {
            res.add(ArrayList(sub))
            return
        }

        sub.add(nums[i])
        backtrack(i + 1)

        sub.removeAt(sub.size - 1)
        backtrack(i + 1)
    }

    return res
}

fun main() {
    
}