class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            target = 0-nums[i]
            st = i + 1
            end = len(nums) - 1
            while st < end:
                s = nums[st] + nums[end]
                if s == target:
                    temp = [nums[i] , nums[st],nums[end]]
                    if temp not in ans:
                        ans.append(temp)
                    st += 1
                    end -= 1
                elif s < target:
                    st += 1
                else:
                    end -= 1
          
        return ans
        
         
            
        