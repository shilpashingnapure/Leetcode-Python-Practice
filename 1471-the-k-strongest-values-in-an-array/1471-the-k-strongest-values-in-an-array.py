class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ans = []
        count = 0
        i = 0
        n = len(arr)
        j = n - 1
        m = (n-1)//2
        arr.sort()
        m = arr[m]
        while i <= j and count < k:
            a = arr[i]
            b = arr[j]
            if abs(a-m) > abs(b-m):
                ans.append(a)
                i += 1
            elif abs(a-m) == abs(b-m) and a > b:
                ans.append(a)
                i += 1
            else:
                ans.append(b)
                j -= 1
            count += 1
        
        return ans
        