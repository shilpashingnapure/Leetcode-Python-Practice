class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = j = 0
        zero = 0
        count = 0
        ans = 0
        while j < len(nums):
            if nums[j] == 0:
                zero += 1
            if nums[j] == 1:
                count += 1
            if zero < 1:
                j += 1
            else:
                ans = max(ans , count)
                
                while zero > 1:
                    if nums[i] == 0:
                        zero -= 1
                    elif nums[i] == 1:
                        count -= 1
                    i += 1
                j += 1
        if zero == 0:
            return len(nums)-1
        return ans
        