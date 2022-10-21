class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
       
       
        while len(nums) != 1:
            n = len(nums)
            i = 0
            ans = []
            while i < len(nums) // 2:

                if i % 2 == 0:
                    ans.append(min(nums[2*i] , nums[2*i+1]))
                else:
                    ans.append(max(nums[2*i] , nums[2*i+1]))
                i += 1
            nums = ans
            
            
            
        
            
            
        return nums[0]