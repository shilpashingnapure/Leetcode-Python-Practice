class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr = []
        i = j = 0
        ans = []
        while j < len(nums):
            arr.append(nums[j])
            if j < k-1:
                j += 1
            elif j-i+1 == k:
                array = sorted(arr)
                value = 0
                if k % 2 == 0:
                    m = k // 2
                    value = (array[m-1] + array[m]) / 2
                else:
                    value = array[k//2]
                ans.append(value)
                if nums[i] in arr:
                    arr.pop(0)
                i += 1
                j += 1
        return ans