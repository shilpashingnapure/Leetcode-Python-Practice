class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if self.checkpalindrome(i):
                return i
        return ""
    def checkpalindrome(self , s):
        mid = len(s)//2
        for i in range(mid+1):
            if(s[i] != s[len(s)-1-i]):
                return False
        return True