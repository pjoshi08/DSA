class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = expression
        i = 0  # shared index

        def helper():  # no need to pass in index because it is shared
            nonlocal i
            c = s[i]
            i += 1
            if c == "t":
                return True
            if c == "f":
                return False

            i += 1  # skip opening bracket as c is one of !, & or |
            if c == "!":
                res = not helper()
                i += 1  # to skip closing bracket
                return res

            # reaching here means c is & or |
            children = []
            while s[i] != ")":
                if s[i] != ",":
                    children.append(helper())
                else:
                    i += 1

            i += 1
            if c == "&":
                return all(children)
            if c == "|":
                return any(children)

        return helper()