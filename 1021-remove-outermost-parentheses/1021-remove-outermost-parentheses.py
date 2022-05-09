class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        p = ""
        count = 0
        lst = []
        for i in s:
            if(i == "("):
                count += 1
            else:
                count -= 1
            p += i    
            if(count == 0):
                lst.append(p)
                p = ""
        ans = ""
        for i in lst:
            string = i[1:len(i)-1]
            ans += string
        return ans