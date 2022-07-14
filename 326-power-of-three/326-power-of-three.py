class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def powerofthree(n , x):
            if(3**x == n):
                return True
            if(3**x > n):
                return False
            return powerofthree(n , x+1)
        return powerofthree(n , 0)