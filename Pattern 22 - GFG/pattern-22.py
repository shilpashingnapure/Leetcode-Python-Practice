#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        mat = [[0] * (N+N-1) for i in range((N+N)-1)]
        n = len(mat)
        m = len(mat[0])
        count = 0
        top = 0 
        left = 0
        bottom = n-1
        right = m-1
        while count < n * m:
            for i in range(left , right+1):
                mat[top][i] = str(N)
                count += 1
            top += 1
            for i in range(top , bottom+1):
                mat[i][right] = str(N)
                count += 1
            right -= 1
            for i in range(right , left-1 , -1):
                mat[bottom][i] = str(N)
                count += 1
            
            bottom -= 1
            for i in range(bottom , top-1 , -1):
                mat[i][left] = str(N)
                count += 1
            left += 1
            
            N -= 1
        
        for i in mat:
            print(" ".join(i))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends