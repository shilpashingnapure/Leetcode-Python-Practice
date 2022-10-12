class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = 1
        k = 2
        m = 0
        while k < len(nums):
            if nums[i] + nums[j] > nums[k]:
                m = max(m , nums[i] + nums[j] + nums[k])
            i += 1
            j += 1
            k += 1
        return m
        