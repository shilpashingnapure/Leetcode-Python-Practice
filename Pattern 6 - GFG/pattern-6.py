#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N , 0 , -1):
            num = 1
            temp = []
            for j in range(i):
                temp.append(str(num))
                num += 1
            print(" ".join(temp))

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