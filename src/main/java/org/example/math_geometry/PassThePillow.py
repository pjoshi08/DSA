class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t, person = 0, 1
        direction = 1

        while t < time:
            if 0 < person + direction <= n:
                person += direction
                t += 1
            else:
                direction *= -1

        return person