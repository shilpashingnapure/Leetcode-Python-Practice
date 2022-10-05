class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        eq = []
        after = []
        for i in nums:
            if i < pivot:
                before.append(i)
            elif i == pivot:
                eq.append(i)
            else:
                after.append(i)
        return before + eq + after