class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        mid = len(s)//2
        a = s[0:mid]
        b = s[mid:len(s)]
        acount = 0
        bcount = 0
        for i in range(mid):
            if a[i] in "aeiou":
                acount += 1
            if b[i] in "aeiou":
                bcount += 1
        return acount == bcount
       