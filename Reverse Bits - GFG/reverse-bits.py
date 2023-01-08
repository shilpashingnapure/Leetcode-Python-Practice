#User function Template for python3

class Solution:
    def reversedBits(self, X):
        # code here 
        b = "{:032b}".format(X)[::-1]
        
        return int(b,2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends