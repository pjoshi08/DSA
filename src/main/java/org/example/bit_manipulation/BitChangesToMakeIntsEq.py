class Solution:
    def minChanges(self, n: int, k: int) -> int:
        # Convert n and k to binary strings
        n_bin = bin(n)[2:]
        k_bin = bin(k)[2:]

        # Pad the shorter binary string with leading zeros
        max_len = max(len(n_bin), len(k_bin))
        n_bin = n_bin.zfill(max_len)
        k_bin = k_bin.zfill(max_len)

        # Count the number of differing bits
        changes = 0
        for i in range(max_len):
            if n_bin[i] == '1' and k_bin[i] == '0':
                changes += 1
            elif n_bin[i] == '0' and k_bin[i] == '1':
                return -1

        return changes

    def minChanges(self, s: str) -> int:
        res = 0

        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                res += 1

        return res


# Example usage:
solution = Solution()
print(solution.minChanges(13, 4))  # Output: 2
print(solution.minChanges(21, 21))  # Output: 0
print(solution.minChanges(14, 13))  # Output: -1
