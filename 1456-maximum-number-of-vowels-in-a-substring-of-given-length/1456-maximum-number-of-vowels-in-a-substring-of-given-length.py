class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = j = 0
        count = 0
        vowels = "aeiou"
        m = 0
        while j < len(s):
            if s[j] in vowels:
                count += 1
            if j < k-1:
                j += 1
            elif j - i + 1 == k:
                m = max(m , count)
                if s[i] in vowels:
                    count -= 1
                i += 1
                j += 1
        return m
        