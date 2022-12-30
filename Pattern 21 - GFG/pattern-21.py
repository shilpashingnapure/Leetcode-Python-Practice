#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            temp = ''
            for j in range(N):
                if (i == 0 or i == N-1 or j == 0 or j == N-1):
                    temp += '*'
                else:
                    temp += ' '
            print(temp)


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