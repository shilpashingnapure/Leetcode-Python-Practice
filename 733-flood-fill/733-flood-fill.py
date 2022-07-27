class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        color_mat = image[sr][sc]
        # if color_mat == color:return image
        def dfs(row , col):
            if image[row][col] == color_mat and color_mat != color:
                image[row][col] = color
                if row >= 1: dfs(row-1 , col)
                if row + 1 < r: dfs(row + 1 , col)
                if col >= 1 : dfs(row , col - 1)
                if col + 1 < c : dfs(row , col+1)
        dfs(sr , sc)
        return image
                
                
            
                
        
        
       