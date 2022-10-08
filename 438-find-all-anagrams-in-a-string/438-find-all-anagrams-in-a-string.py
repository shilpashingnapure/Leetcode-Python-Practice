class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = Counter(p)
        i = j = 0
        count = []
        while j < len(s):
            if s[j] in d:
                d[s[j]] -= 1
            if j < len(p)-1:
                j += 1
            elif j - i + 1 == len(p):
                lst = list(d.values())
                if len(set(lst)) == 1 and lst[0] == 0:
                    count.append(i)
                if s[i] in d:
                    d[s[i]] += 1
                i += 1
                j += 1
        return count