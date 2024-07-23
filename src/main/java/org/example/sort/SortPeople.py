from typing import List


class Solution:
    # Bubble sort, O(n^2)
    def sortPeople2(self, names: List[str], heights: List[int]) -> List[str]:
        merged = list(zip(heights, names))
        n = len(merged)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if merged[i][0] < merged[j][0]:
                    tmp = merged[i]
                    merged[i] = merged[j]
                    merged[j] = tmp
        return [m[1] for m in merged]

    # merge sort, O(nlogn)
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        merged_list = list(zip(heights, names))
        sorted_list = self.merge_sort(merged_list)

        return [x[1] for x in sorted_list]

    def merge_sort(self, array: List[int]) -> List[int]:
        n = len(array)
        if n < 2: return array

        mid = n // 2

        return self.merge(
            left=self.merge_sort(array[:mid]),
            right=self.merge_sort(array[mid:]))

    def merge(self, left, right):
        # If left array is empty, there is nothing to be merged, return right array
        if not left: return right
        # similarly if right is empty, return left
        if not right: return left

        res = []
        l = r = 0
        while len(res) < len(left) + len(right):
            # have to sort is descending order
            if left[l][0] >= right[r][0]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

            # if we have reached the end of one array, append the other array to the res
            if l == len(left):
                res.extend(right[r:])
                break
            if r == len(right):
                res.extend(left[l:])
                break

        return res
