class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,mx = 0,0
        for r , n in enumerate(nums):
            k -= (1-n)
            if k < 0:
                k += (1-nums[l])
                l += 1
            mx = max(mx , r-l+1)
        return mx
            
    #     i = 0
    #     j = 1
    #     m = 0
    #     while j < len(nums):
    #         check , length = self.checkzero(i,j,nums,k)
    #         if(check):
    #             j+=1
    #             m = max(m,length)
    #         else:
    #             i+=1
    #             j+=1
    #     return m
    # def checkzero(self , start , end , arr , k):
    #     d = {0:0 , 1:0}
    #     for i in range(start , end+1):
    #         # print(arr[i])
    #         d[arr[i]] += 1
    #     return [d[0] <= k , d[0] + d[1]]
        