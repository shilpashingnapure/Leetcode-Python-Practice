class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        
        #using startswith function
        # for i in words:
        #     if i.startswith(pref):
        #         count += 1
                
        #without using function
        for i in words:
            if(i[0:len(pref)] == pref):
                print(i[0:len(pref)])
                count+= 1
        return count