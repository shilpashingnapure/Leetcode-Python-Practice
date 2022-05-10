class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # matrix = [["white" for j in range(8)] for i in range(8)]
        # for i in range(8):
        #     for j in range(8):
        #         if i % 2 == 0 and j%2 == 0:
        #             matrix[i][j] = "black"
        #         if i%2 == 1 and j % 2 == 1:
        #             matrix[i][j] = "black"
        d = "abcdefgh"
        x = d.index(coordinates[0])
        y = int(coordinates[1])-1
        # return matrix[x][y] == "white"
    
        #using math method
        if(x + y)%2 == 0:return False
        return True
        