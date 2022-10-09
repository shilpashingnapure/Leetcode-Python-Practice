class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = j = 0
        d = Counter()
        ans = 0
        while j < len(fruits):
            d[fruits[j]] += 1
            if len(d) <= 2:
                ans = max(ans , j - i + 1)
                j += 1
            else:
                while len(d) > 2:
                    d[fruits[i]] -= 1
                    if d[fruits[i]] == 0:
                        del d[fruits[i]]
                    i += 1
                j += 1
        return ans
        