class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        #find out index of begin with high , low , same
        
        arr = [0] * len(nums)
        low = eq = 0
        for i in nums:
            if i < pivot:
                low+=1
            elif i == pivot:
                eq += 1
        high = low + eq
        eq = low
        low = 0
        for i in nums:
            if i < pivot:
                arr[low] = i
                low+=1
            elif i == pivot:
                arr[eq] = i
                eq += 1
            else:
                arr[high] = i
                high += 1
        return arr
                
        # before = []
        # eq = []
        # after = []
        # for i in nums:
        #     if i < pivot:
        #         before.append(i)
        #     elif i == pivot:
        #         eq.append(i)
        #     else:
        #         after.append(i)
        # return before + eq + after