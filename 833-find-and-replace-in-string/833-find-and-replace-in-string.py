class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        ans = ""
        j = 0
        while j < len(s):
            if j in indices:
                
                #if index is present then we getting index in indices list
                index = indices.index(j)
                
                #finding substring in s 
                print(s[j:j+len(sources[index])] , sources[index])
                
                #if substring is equal to sources and j equal to indices element add target value and increment by length of substring
                if s[j:j+len(sources[index])] == sources[index] and j == indices[index]:
                    ans += targets[index]
                    j += len(sources[index])
                    
                #nothing to do
                else:
                    ans += s[j]
                    j += 1
                    
            #nothing to do increment by 1
            else:
                ans += s[j]
                j += 1
        return ans
                
            