class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        i = j = 0
        m = inf
        nums.sort()
        while j < len(nums):
            if j < k-1:
                j += 1
            elif j - i + 1 == k:
               
                m = min(m , nums[j]-nums[i])
                i += 1
                j += 1
        return m
        