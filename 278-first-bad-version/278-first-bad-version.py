# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        ans = n  
        while(left <= n):
            mid = ((left + n) // 2)
            isbad = isBadVersion(mid)
            if isbad:
                ans = mid
                n = mid - 1
            else:
                left = mid + 1
            
        return ans
    
#     1 2 3 
    
#     n = 1
      # 1 + 1 = 2 // 2 -> 1
     
    
    
    
    
    
    
    
    
    
    
    
     
    
    
    
    
    
            
                
      