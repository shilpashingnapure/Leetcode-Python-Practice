class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        countFreshOrange = 0 
        N = len(grid)
        M = len(grid[0])
        
        que = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    countFreshOrange += 1
                    
                if grid[i][j] == 2:
                    que.append((i , j))
                    
                    
        if countFreshOrange == 0:return 0
        
        def bfs(r , c):
            count = 0
            if r >= 1 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                que.append((r-1 , c))
                count += 1
            if r+1 < N and grid[r+1][c] == 1:
                grid[r+1][c] = 2
                que.append((r+1 , c))
                count += 1
                
            if c >= 1 and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                que.append((r , c-1))
                count += 1
                
            if c+1 < M and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                que.append((r , c+1))
                count += 1
            
            return count
        ans = 0
        while que and countFreshOrange > 0:
            
            ans += 1
            for i in range(len(que)):
                r,c = que.pop(0)
                m = bfs(r,c)
                countFreshOrange -= m
            
            
            
        if countFreshOrange != 0: return -1             
        return ans
 
    
    
    
    
    
    
    
   