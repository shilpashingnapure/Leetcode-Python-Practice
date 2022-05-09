class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        for i in range(0 , len(rings) , 2):
            pos = rings[i+1]
            ring = rings[i]
            if(pos in d):
                s = d[pos]
                s.add(ring)
                
            else:
                d[pos] = {ring}
        
        count = 0
        for key , value in d.items():
            if(len(value) == 3):
                count += 1
        return count
            
        
        
        
            
            