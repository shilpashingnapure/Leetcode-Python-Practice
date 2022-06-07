class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = sorted(nums1[:m] + nums2[:n]) 
        print(n)
        for i in range(len(nums1)):
            nums1[i] = n[i]
          
             