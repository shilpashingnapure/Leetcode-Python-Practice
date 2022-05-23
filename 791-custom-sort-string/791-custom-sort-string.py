class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        
        arr = []
        new_s = ""
        for i in s:
            if i in d:
                temp = [i , d[i]]
                arr.append(temp)
            else:
                new_s += i
        
        arr.sort(key = lambda a: a[1])
        ans = ""
        for i in arr:
            a = i[0]
            ans += a
        ans += new_s
        return ans
        
                
            
            
                
        