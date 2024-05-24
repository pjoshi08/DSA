from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        ops = {'*', '+', '-'}
        for i, c in enumerate(expression):
            if c in ops:
                s1 = expression[:i]
                s2 = expression[i + 1:]
                res1 = self.diffWaysToCompute(s1)
                res2 = self.diffWaysToCompute(s2)
                for x in res1:
                    for y in res2:
                        if c == '*':
                            res.append(x * y)
                        elif c == '+':
                            res.append(x + y)
                        elif c == '-':
                            res.append(x - y)

        if not res: res.append(int(expression))
        return res


obj = Solution()
expression = "2*3-4*5"
print(obj.diffWaysToCompute(expression))
