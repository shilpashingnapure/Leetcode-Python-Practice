class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        i = j = 0
        d = ""
        count = 0
        num = str(num)
        while j < len(num):
            d += num[j]
            # print(d)
            if j < k-1:
                j += 1
            elif j - i + 1 == k:
                if int(d) != 0 and int(num) % int(d) == 0:
                    count += 1
                
                d = d[1:]
                
                i += 1
                j += 1
        return count
        