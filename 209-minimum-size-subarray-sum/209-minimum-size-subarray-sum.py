class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = 0
        s = 0
        ans = inf
        while j < len(nums):
            s += nums[j]
            if s < target:
                j += 1
            else:
                while s >= target:
                    s -= nums[i]
                    ans = min(ans , j-i+1)
                    i += 1
                    
                j += 1
        if ans == inf:return 0
        return ans
    
    