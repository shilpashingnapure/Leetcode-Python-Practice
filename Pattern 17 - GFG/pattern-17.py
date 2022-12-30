#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        n = 1
        for i in range(N):
            temp = ''
            a = ord('A')
            
            for _ in range(N-i-1):
                temp += ' '
            
            for k in range(n//2 + 1):
                temp += chr(a)
                a += 1
            
            for j in range(n//2):
                a -= 1
                temp += chr(a - 1)
                
            n += 2
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