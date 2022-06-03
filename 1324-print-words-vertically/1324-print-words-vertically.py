class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        
        maxlength = 0
        for i in s:
            maxlength = max(len(i) , maxlength)
        
        for i in range(len(s)):
            if len(s[i]) != maxlength:
                s[i] = list(s[i] + " " * abs(maxlength - len(s[i])))
            else:
                s[i] = list(s[i])
        
        ans = []
        for i in range(len(s[0])):
            arr = ""
            for j in range(len(s)):
                arr += s[j][i]
                
            ans.append(arr.rstrip())
                
        return ans
    
    
    
    