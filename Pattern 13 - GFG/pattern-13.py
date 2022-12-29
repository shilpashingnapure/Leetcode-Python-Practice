#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        num = 1
        for i in range(N):
            temp = []
            for j in range(i+1):
                temp.append(str(num))
                num+=1
            print(' '.join(temp))


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