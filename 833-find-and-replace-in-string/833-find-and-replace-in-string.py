class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        ans = ""
        j = 0
        while j < len(s):
            if j in indices:
                count = indices.index(j)
                print(s[j:j+len(sources[count])] , sources[count])
                
                if s[j:j+len(sources[count])] == sources[count] and j == indices[count]:
                    ans += targets[count]
                    j += len(sources[count])
                else:
                    ans += s[j]
                    j += 1
            else:
                ans += s[j]
                j += 1
        return ans
                
            