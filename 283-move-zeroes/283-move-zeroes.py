class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1 0 1
            # l r
            
          
        
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] == 0 and nums[right] == 0:
                right += 1
            else:
                if nums[left] == 0 and nums[right] != 0:
                    nums[left] , nums[right] = nums[right] , nums[left]
                left += 1
                right += 1
        
                
                