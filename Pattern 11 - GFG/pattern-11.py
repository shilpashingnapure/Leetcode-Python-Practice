#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        num = True
        for i in range(1, N+1):
            if(i % 2 == 0):
                num = False
            else:
                num = True
            temp = ''
            for j in range(i):
                if num:
                    temp += '1 '
                else:
                    temp += '0 '
                num = not(num)
        
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