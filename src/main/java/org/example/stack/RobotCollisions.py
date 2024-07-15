from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        # important to maintain the original order of positions/health
        # but we need to process each robot based on the sorted order of positions
        # below statement sorts the positions but stores the indices based on the lamda
        # If positions =  and indices = [0,1,2,3]
        # For x = 0: positions[0] is 3.
        # For x = 1: positions[1] is 5.
        # For x = 2: positions[2] is 2.
        # For x = 3: positions[3] is 6.
        # So, the values for sorting will be [3, 5, 2, 6].
        # and sorted order of these values is [2, 3, 5, 6], which corresponds to indices [2, 0, 1, 3].
        # For sorted[0] is 2: x = 2.
        # For sorted[1] is 3: x = 0.
        # For sorted[2] is 5: x = 1.
        # For sorted[3] is 6: x = 3.
        indices.sort(key=lambda x: positions[x])
        stack = []

        for cur in indices:
            if directions[cur] == "R":
                stack.append(cur)
            else:
                while stack and healths[cur] > 0:
                    prev = stack.pop()

                    if healths[prev] > healths[cur]:
                        healths[prev] -= 1
                        healths[cur] = 0
                        stack.append(prev)
                    elif healths[prev] < healths[cur]:
                        healths[prev] = 0
                        healths[cur] -= 1
                    else:
                        healths[prev] = 0
                        healths[cur] = 0

        res = []
        for h in healths:
            if h > 0: res.append(h)
        return res


obj = Solution()
positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
print(obj.survivedRobotsHealths(positions, healths, directions))