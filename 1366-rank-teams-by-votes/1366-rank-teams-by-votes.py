class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for vote in votes:
            for j in range(len(vote)):
                if vote[j] not in d:
                    d[vote[j]] = [0] * len(vote)
                d[vote[j]][j] -= 1
        
        ans = sorted(d , key=lambda x : (d[x] , x))
        return "".join(ans)        
                
            