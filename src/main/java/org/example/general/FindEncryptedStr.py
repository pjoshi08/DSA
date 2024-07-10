class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        res = []
        for i in range(n):
            res.append(s[(i + k) % n])
        return ''.join(res)