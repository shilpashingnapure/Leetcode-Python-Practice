#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        zero = []
        one = []
        two = []
        for i in arr:
            if(i == 0):zero.append(i)
            elif (i == 1):one.append(i)
            else:two.append(i)
        arr[:] = zero + one +two    
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends