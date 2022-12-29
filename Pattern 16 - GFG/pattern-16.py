#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        ch = ord('A')
        for i in range(1,N+1):
            print(chr(ch) * i)
            ch += 1


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