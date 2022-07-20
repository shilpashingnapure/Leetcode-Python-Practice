class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Logic Behind -: 
            e.g. 
            
            [1 2 3 4 5 6 7] , k = 3
            1. reverse the 0 to k range [4,3,2,1]
            2. reverse the k to N range [7,6,5]
            it become like [4,3,2,1,7,6,5]
            3. final reverse the whole array
                [5,6,7,1,2,3,4]
        """
        
        #checking if k is greathen len 
        if k > len(nums):
            k = k % len(nums)
            
        #l to r is for 0 to k     
        l = 0
        r = len(nums)-k-1 
        
        #l1 to r1 is for k to N
        l1 = len(nums) - k  
        r1 = len(nums) - 1  
        
        #reversing both 0 to k and k to N
        while l <= r and l1 <= r1:
            nums[l] , nums[r] = nums[r] , nums[l]
            nums[l1] , nums[r1] = nums[r1] , nums[l1]
            l += 1
            r -= 1
            l1 += 1
            r1 -= 1
        
        #checking if 0 to k range still not statifiy condition 
        while l <= r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1
        
        #checking if k to N range still not statifiy condition
        while l1 < r1:
            nums[l1] , nums[r1] = nums[r1] , nums[l1]
            l1 += 1
            r1 -= 1
        
        #after done reversing whole array 
        left = 0
        right = len(nums) - 1
        while left <= right:
            nums[left] , nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
        
    
        

        
        
            
         
        
        
        
        
        