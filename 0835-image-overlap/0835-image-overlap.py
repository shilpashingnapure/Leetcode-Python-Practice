class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        d = Counter()
        a = []
        b = []
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j] == 1:
                    a.append([i,j])
                if img2[i][j] == 1:
                    b.append([i,j])
        ans = 0
        for x in a:
            for y in b:
                v = (y[0] - x[0] , y[1] - x[1])
                d[v] += 1
                ans = max(d[v] , ans)
        return ans