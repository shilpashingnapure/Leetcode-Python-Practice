class Solution:
    def numOfStrings(self, patterns: List[str], words: str) -> int:
        count = 0
        # substrings = []
        # for i in range(len(words)):
        #     bag = ""
        #     for j in range(i , len(words)):
        #         bag += words[j]
        #         if bag not in substrings:
        #             substrings.append(bag)
        
        for i in patterns:
            if i in words:
                count+= 1
        return count