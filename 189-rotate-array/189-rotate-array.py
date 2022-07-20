class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        l = 0
        r = len(nums)-k-1 
        
        l1 = len(nums) - k  
        r1 = len(nums) - 1  
        
        print(l , r)
        print(l1 , r1)
        
        while l <= r and l1 <= r1:
            nums[l] , nums[r] = nums[r] , nums[l]
            nums[l1] , nums[r1] = nums[r1] , nums[l1]
            
           
            l += 1
            r -= 1
            l1 += 1
            r1 -= 1
        
        while l <= r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1
        
        while l1 < r1:
            nums[l1] , nums[r1] = nums[r1] , nums[l1]
            l1 += 1
            r1 -= 1
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
        return nums
    
        
#         0 4
#         1 2 3 4 5
#         5 4 3 2 1
#         6 7
#         7 6
        
#         5 4 3 2 1 7 6 
        # 6 7 1 2 3 4 5
    
    
        
      # 1  2 3 4 5 6
      # 1 6 5 4 3 2
        
        
            
         
        
        
        
        
        