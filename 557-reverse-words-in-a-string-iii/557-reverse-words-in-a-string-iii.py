class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = [i[::-1] for i in s]
        return " ".join(ans)
        