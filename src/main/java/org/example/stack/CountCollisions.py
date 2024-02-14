
# Count Collisions on a road: https://leetcode.com/problems/count-collisions-on-a-road/description/

class Solution:

    # Better solution, lesser time and O(1) memory
    def countCollisions(self, directions: str) -> int:
        count, n = 0, len(directions)
        i, carsTakingRight = 0, 0
        while i < n and directions[i] == "L":  # skip cars taking left form the start that will never collide
            i += 1

        while i < n:
            if directions[i] == "R":
                carsTakingRight += 1
            else:
                count += carsTakingRight if directions[i] == "S" else carsTakingRight + 1
                carsTakingRight = 0
            i += 1
        return count

        # Accepted but slower
    def countCollisions2(self, directions: str) -> int:
        count = 0
        stack = [directions[0]]

        for d in directions[1:]:
            if stack[-1] == "R" and (d == "L" or d == "S"):
                stack.pop()
                count += 2 if d == "L" else 1

                while stack and stack[-1] == "R":
                    stack.pop()
                    count += 1
                stack.append("S")

            elif d == "L" and stack[-1] == "S":
                count += 1
            elif d == "S":
                stack = [d]
            else:
                stack.append(d)
        return count


obj = Solution()
#directions = "RLRSLL"
directions = "LLRR"
print(obj.countCollisions(directions))
