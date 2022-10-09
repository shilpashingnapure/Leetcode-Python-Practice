class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = Counter(t)
        i = j = 0
        count = len(d)
        m = inf
        ans = ""
        while j < len(s):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    count -= 1
            if count > 0:
                j += 1
            elif count == 0:
                while count != 1:
                    if j-i+1 < m:
                        ans = s[i:j+1]
                        m = j-i+1
                    # m = min(m , j-i+1)
                    if s[i] in d:
                        d[s[i]] += 1
                    if d[s[i]] > 0:count += 1
                    i += 1
                j += 1
        return ans