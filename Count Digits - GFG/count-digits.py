#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        Num = N
        while Num != 0:
            mod = Num % 10
            if(mod != 0 and N % mod == 0):count+=1
            Num = Num // 10
        
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends