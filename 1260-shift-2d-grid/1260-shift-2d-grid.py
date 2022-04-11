class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        for _ in range(k):
            p = grid[-1][-1]
            for row in range(m):
                for col in range(n):
                    temp = grid[row][col]
                    grid[row][col] = p
                    p = temp
        return grid
        