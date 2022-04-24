class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.station = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName , t] 

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s = ""
        time = t
        if id in self.check:
            s += self.check[id][0]
            time -= self.check[id][1]
        s += "-" + stationName
        
        if(s in self.station):
            self.station[s].append(time)
        else:    
            self.station[s] = [time]
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s = startStation + "-" + endStation
        if s in self.station:
            return sum(self.station[s])/ len(self.station[s])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)