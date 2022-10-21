class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        #invert the string
        def invert(s):
            ans = ""
            for i in s:
                if i == '0':
                    ans += '1'
                else:
                    ans += '0'
            return ans
        
        #find nkth bit
        def findK(n):
            if n == 1:
                return "0"
            return findK(n-1) + '1' + invert(findK(n-1))[::-1]
            
        return findK(n)[k-1]