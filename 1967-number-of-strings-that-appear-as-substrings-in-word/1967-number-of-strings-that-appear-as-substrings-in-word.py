class Solution:
    def numOfStrings(self, patterns: List[str], words: str) -> int:
        count = 0
        substrings = []
        for i in range(len(words)):
            bag = ""
            for j in range(i , len(words)):
                bag += words[j]
                substrings.append(bag)
        
        for i in patterns:
            if i in substrings:
                count+= 1
        return count