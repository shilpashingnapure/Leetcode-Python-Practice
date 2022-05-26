class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = []
        text = text.split(" ")
        for i in text:
            
            arr.append([i.lower() , len(i)])
        
        arr.sort(key=lambda  x : x[1])
        arr = [i[0] for i in arr]
        s = " ".join(arr)
        return s[0].upper() + s[1:]