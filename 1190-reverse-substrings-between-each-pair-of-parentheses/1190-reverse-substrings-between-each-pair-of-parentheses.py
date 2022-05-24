class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                
            elif s[i] == ")":
                
                start = stack.pop()
                end = i
                rev = s[start+1:end]
                
                s[start+1:end] = rev[::-1]
                   
        return ''.join(s).replace("(" , '').replace(")" , '')
                
                 
        
        
     