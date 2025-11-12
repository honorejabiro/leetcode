"""
- Check in
    - Customer can only check into on place at a time
    - so maybe a hashed storage?


- Check Out
    - simply check out

- station: {set of checked in customers: (customer_id, timestamp)}

- getAverageTime
    - all average times from both: directly

- Try to make it like relational databases

- check_in table: [(id, stationName, t)] 
- check out: [(id, from, stationName, t)]

- averageTime
"""


class UndergroundSystem:

    def __init__(self):
      self.check_ins = {}
      self.check_outs = defaultdict(int)
      self.number_of_trips = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_ins:
            return

        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.check_ins:
            return

        starting_station, starting_time = self.check_ins[id]
        del self.check_ins[id]
        self.check_outs[(starting_station, stationName)] += t- starting_time 
        self.number_of_trips[(starting_station, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.check_outs[(startStation, endStation)] / self.number_of_trips[(startStation, endStation)]
                

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
