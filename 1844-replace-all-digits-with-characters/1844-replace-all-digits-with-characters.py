class Solution:
    def replaceDigits(self, s: str) -> str:
        lower = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        
        for i in range(0 , len(s)):
            if(s[i].isnumeric()):
                index = lower.index(s[i-1])
                index = index + int(s[i])
                ans += lower[index]
            else:
                ans += s[i]
        return ans
        
#         "a1c1e1"
        
#         "abcde"
        
#         shift("a" , 1) -> b
#         shift("c" , 1) -> d
#         shift("e" , 1) -> "f"