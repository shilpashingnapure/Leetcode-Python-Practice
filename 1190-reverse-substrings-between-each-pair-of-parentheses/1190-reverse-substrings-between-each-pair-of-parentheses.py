class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        stack = []   #<- storing the open parenthese indexs
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                
            elif s[i] == ")":
                
                #index of open parentheses
                start = stack.pop()
                
                #index of closing parenthese
                end = i
                
                #reversing the substring between open and closing parenthese
                rev = s[start+1:end]
                
                #updating that reverse substring
                s[start+1:end] = rev[::-1]
                   
        #removing parenthese in string            
        return ''.join(s).replace("(" , '').replace(")" , '')
                
                 
        
        
     