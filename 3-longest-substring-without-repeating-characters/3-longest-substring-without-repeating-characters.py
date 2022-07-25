class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        largetslen = 0
        m = 0
        while right < len(s):
            check , l = self.checkdup(s[left:right+1])
            if(check):
                left += 1
            else:
                m = max(m , l)
                right += 1
        return m
    
    def checkdup(self, s):
        d = Counter(s).values()
        return max(d) > 1 , len(d)
        
    