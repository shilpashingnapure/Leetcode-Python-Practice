class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def helper(nums , target , s , e):
            if s > e:
                return -1
            mid = s + (e-s) // 2
            
            if nums[mid] == target:return mid
            if nums[mid] > target:
                return helper(nums , target , s , mid - 1)
            else:
                return helper(nums , target , mid + 1 , e)
        return helper(nums , target , 0 , len(nums)-1)
        
    
    
    
    