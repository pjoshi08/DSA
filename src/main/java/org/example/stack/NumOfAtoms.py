from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        n = len(formula)
        index = 0

        while index < n:
            if formula[index] == "(":
                stack.append(defaultdict(int))
                index += 1
            elif formula[index] == ")":
                curMap = stack.pop()
                multiplier = ""
                index += 1

                while index < n and formula[index].isdigit():
                    multiplier += formula[index]
                    index += 1

                if multiplier:
                    multiplier = int(multiplier)
                    # increase count for all atoms between brackets based on multiplier
                    for atom in curMap:
                        curMap[atom] *= multiplier

                # add the count for all atoms between brackets to the outer atoms
                for atom in curMap:
                    stack[-1][atom] += curMap[atom]
            else:  # add the cur atom to the top of the dict on stack
                atom = formula[index]
                count = ""
                index += 1

                # check if the atom has lowercase chars in its name
                while index < n and formula[index].islower():
                    atom += formula[index]
                    index += 1

                # capture the count of the cur atom
                while index < n and formula[index].isdigit():
                    count += formula[index]
                    index += 1

                if count == "":
                    count = 1
                else:
                    count = int(count)

                stack[-1][atom] += count

        res = ""
        sortedDict = dict(sorted(stack[0].items()))
        for atom in sortedDict:
            res += atom
            if sortedDict[atom] > 1:
                res += str(sortedDict[atom])

        return res
