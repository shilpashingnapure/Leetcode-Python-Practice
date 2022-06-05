class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        ans = ""
        j = 0
        while j < len(s):
            if j in indices:
                index = indices.index(j)
                print(s[j:j+len(sources[index])] , sources[index])
                
                if s[j:j+len(sources[index])] == sources[index] and j == indices[index]:
                    ans += targets[index]
                    j += len(sources[index])
                else:
                    ans += s[j]
                    j += 1
            else:
                ans += s[j]
                j += 1
        return ans
                
            