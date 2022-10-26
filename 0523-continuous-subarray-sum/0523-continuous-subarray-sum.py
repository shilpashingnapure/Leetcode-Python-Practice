class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            r = s % k
            if r not in d:
                d[r] = i + 1
            elif d[r] < i:
                return True
        False
        
        
        
        