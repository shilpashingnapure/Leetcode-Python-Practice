class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        arr = [[plantTime[i] , growTime[i]] for i in range(len(plantTime))]
        arr.sort(key=lambda x:-x[1])
        s = 0
        ans = 0
        for i in range(len(arr)):
            s += arr[i][0]
            ans = max(ans , s + arr[i][1])
        return ans