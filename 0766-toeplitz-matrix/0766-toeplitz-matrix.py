class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        M = len(matrix[0])
        for i in range(M-1 , -1 , -1):
            prev = ''
            for j in range(N):
                if i + j < M:
                    # print(matrix[j][i+j])
                    if prev == '':
                        prev=matrix[j][i+j]
                    elif prev != matrix[j][i+j]:return False
        
        for i in range(1 , N):
            prev = ''
            print(i , N)
            for j in range(M):
                # print(i+j)
                if i+j < N:
                    # print(matrix[i+j][j])
                    if prev == '':
                        prev = matrix[i+j][j]
                    elif prev != matrix[i+j][j]:
                        return False
        return True
        # 41 45
        # 81 41
        # 73 81
        # 47 73
        # 0  47
        # 79 76
 