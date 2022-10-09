class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        i = j = 0
        m = inf
        nums.sort()
        while j < len(nums):
            if j < k-1:
                j += 1
            elif j - i + 1 == k:
                a = min(nums[i:j+1])
                b = max(nums[i:j+1])
                m = min(m , b-a)
                i += 1
                j += 1
        return m
        