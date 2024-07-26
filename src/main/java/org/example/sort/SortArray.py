from typing import List


class Solution:
    # Merge sort, sort in place, faster
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):
            left, right = arr[L:M + 1], arr[M + 1:R+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r: return arr

            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        return mergeSort(nums, 0, len(nums) - 1)

    # slower and takes extra memory for res arr
    def sortArray2(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, array):
        n = len(array)
        if n < 2: return array

        mid = n // 2
        return self.merge(
            left=self.merge_sort(array[:mid]),
            right=self.merge_sort(array[mid:])
        )

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        res = []
        l = r = 0
        while len(res) < len(left) + len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

            if l == len(left):
                res.extend(right[r:])
                break
            if r == len(right):
                res.extend(left[l:])
                break
        return res

