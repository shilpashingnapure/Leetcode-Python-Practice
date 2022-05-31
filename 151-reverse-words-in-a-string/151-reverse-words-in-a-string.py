class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s)
        s = s.split(" ")
        ans = filter(lambda x : x != "" , s)
        return " ".join(list(ans)[::-1])
        