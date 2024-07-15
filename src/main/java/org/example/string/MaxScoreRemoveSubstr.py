from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pref = ""
        if x >= y:
            pref = ["ab", x]
            non_pref = ["ba", y]
        else:
            pref = ["ba", y]
            non_pref = ["ab", x]

        def calculate(s: str, pref: List[str]):
            stack = []
            score = 0
            for c in s:
                if c == pref[0][1]:
                    if stack and stack[-1] == pref[0][0]:
                        stack.pop()
                        score += pref[1]
                    else:
                        stack.append(c)
                else:
                    stack.append(c)

            return score, "".join(stack)

        total, s = calculate(s, pref)   # one pass to captured preferred substring
        total2, s = calculate(s, non_pref)
        return total
