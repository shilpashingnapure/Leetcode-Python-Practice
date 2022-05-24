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
                rev = ""
                for j in range(end-1 , start , -1):
                    rev += s[j]
                s[start+1:end] = rev
                   
        return ''.join(s).replace("(" , '').replace(")" , '')
                
                 
        
        
     