class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [-1] * len(days)
        ans = self.recurv(days , costs , 0 , dp )
        return ans
        
    def recurv(self,days , costs , day,dp ):
        if day >= len(days):return 0
        
        if(dp[day] != -1):return dp[day]
    
        day1 = self.recurv(days , costs , day + 1,dp) + costs[0]
        d = day
        for i in range(day , len(days)):
            if days[i] >= days[day] + 7:break
            d += 1
        day7 = self.recurv(days , costs , d , dp) + costs[1]
        
        d = day
        for i in range(day , len(days)):
            if days[i] >= days[day] + 30:break
            d += 1
        day30 = self.recurv(days , costs , d , dp) + costs[2]
        
        dp[day] = min(day1 , day7 , day30)
        return dp[day]
        