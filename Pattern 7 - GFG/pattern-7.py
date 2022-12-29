#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        num = 1
        for i in range(1,N+1):
            temp = ''
            for _ in range(N-i):
                temp += ' '
            for k in range(num // 2+1):
                temp += '*'
            for j in range(num // 2):
                temp += "*"
            num += 2
            print(temp)
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends