import collections


class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for r in range(n):
            for c in range(n):
                if (matrix[r][c] in rows[r] or
                        matrix[r][c] in cols[c]):
                    return False
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
        return True


obj = Solution()
matrix = [[1, 1, 1], [1, 2, 3], [1, 2, 3]]
print(obj.checkValid(matrix))
