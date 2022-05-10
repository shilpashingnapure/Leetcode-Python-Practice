class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = word
        index = None
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break;
        
        if(index != None):
            a = word[0:index+1][::-1]
            b = word[index+1:len(word)]
            ans = a + b
        return ans
                
        