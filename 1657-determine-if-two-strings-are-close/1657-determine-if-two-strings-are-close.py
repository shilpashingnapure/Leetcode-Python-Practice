class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = Counter(word1)
        d2 = Counter(word2)
        key1 , key2 = sorted(d1.keys()) , sorted(d2.keys())
        val1 , val2 = sorted(d1.values()) , sorted(d2.values())
       
        return key1 == key2 and val1 == val2