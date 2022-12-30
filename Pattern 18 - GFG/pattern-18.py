#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        
        for i in range(1,N+1):
            char = ord('A') + (N-1)
            temp = ''
            for j in range(i):
                temp += chr(char - j) + " "
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