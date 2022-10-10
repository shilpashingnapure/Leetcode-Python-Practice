class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = j = 0
        d = Counter()
        s = 0
        ans = 0
        while j < len(nums):
            s += nums[j]
            d[nums[j]] += 1
            
            if len(d) == j - i + 1:  
                ans = max(ans,s)
                # print(s , d , j , i)
            elif len(d) != j-i+1:
                while len(d) != j - i + 1:
                    d[nums[i]] -= 1
                    if d[nums[i]] == 0:
                        del d[nums[i]]
                   
                    s -= nums[i]
                    i += 1
            
            j += 1
        return ans
     