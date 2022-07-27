class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        
        def dfs(r , c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 0:
                return 0
            
            #we are replacing 1 to zero , so we don't see alredy edges
            grid[r][c] = 0
            top = dfs(r-1 , c)
            down = dfs(r+1 , c)
            left = dfs(r , c -1 )
            right = dfs(r , c + 1)
            return 1 + top + down + left + right 
        ans = 0
        for i in range(R):
            for j in range(C): 
                if grid[i][j] == 1:
                    m = dfs(i , j)
                    ans = max(m , ans)
        return ans
                    