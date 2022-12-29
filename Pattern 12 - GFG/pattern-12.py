#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        
        for i in range(1 , N+1):
            temp = ''
            for j in range(1,i+1):
                temp += str(j) + " "
        
            temp += (N-i) * '  '
            for _ in range(N-i , 0 , -1):
                temp += '  '
            
            for k in range(i , 0 , -1):
                temp += str(k) + ' '
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