class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        return not(len(Counter(nums).keys()) == len(nums))
        