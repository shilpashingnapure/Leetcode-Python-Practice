class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(set(dictionary))
        arr = sentence.split(" ")
        ans = []
        for i in arr:
            a = i
            for j in dictionary:
                if(i.startswith(j)):
                    a = j
                    break
                    
            ans.append(a)
        return " ".join(ans)
            
                    
                