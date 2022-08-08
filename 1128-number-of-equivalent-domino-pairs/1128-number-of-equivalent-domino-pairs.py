class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        seen = []
        for i in dominoes: 
            s = tuple(sorted(i))
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        c = 0
        for k , v in d.items():
            c += v * (v-1)//2
        return c