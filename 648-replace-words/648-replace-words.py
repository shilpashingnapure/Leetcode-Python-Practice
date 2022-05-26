class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # dictionary = sorted(dictionary)
        arr = sentence.split(" ")
        for i in range(len(arr)):
            for j in dictionary:
                if(arr[i].startswith(j)):
                    arr[i] = j
                    
           
        return " ".join(arr)
            
                    
                