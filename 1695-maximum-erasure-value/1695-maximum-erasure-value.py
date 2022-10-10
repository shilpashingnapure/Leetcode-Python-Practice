class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        i = j = 0
        arr = set()
        s = 0
        m = 0
        while j < len(nums):
            if nums[j] not in arr:
                s += nums[j]
                m = max(m , s)
                arr.add(nums[j])
                j += 1
            else:
                s -= nums[i]
                arr.remove(nums[i])
                i += 1
        return m
    
    
#         i = j = 0
#         d = Counter()
#         s = 0
#         ans = 0
#         while j < len(nums):
#             s += nums[j]
#             d[nums[j]] += 1
            
#             if len(d) == j - i + 1:  
#                 ans = max(ans,s)
#             elif len(d) != j-i+1:
#                 while len(d) != j - i + 1:
#                     d[nums[i]] -= 1
#                     if d[nums[i]] == 0:
#                         del d[nums[i]]
                   
#                     s -= nums[i]
#                     i += 1
            
#             j += 1
#         return ans
     