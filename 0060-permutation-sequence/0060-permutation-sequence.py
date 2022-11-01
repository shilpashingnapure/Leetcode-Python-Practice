class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s = ''
        for i in range(n):
            s += str(i+1)
        
        def helper(up , p,ans):
            if up == '':
                ans.append(p)
                return 
            ch = up[0]
            for i in range(len(p)+1):
                first = p[0:i]
                last = p[i:len(p)]
                helper(up[1:] , first + ch + last,ans)
            return ans
        return sorted(helper(s , '',[]))[k-1]