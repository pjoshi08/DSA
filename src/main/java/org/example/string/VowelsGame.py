class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # If vowel count is odd, Alice can remove the whole string and win
        # If vowel count is odd, Alice can remove n - 1 vowels and still win
        # If vowel count is 0, Bob wins
        # So if there is even just one occurence of vowel, Alice wins
        for c in s:
            if c in 'aeiou':
                return True
        return False