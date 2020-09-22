import json

class MapManager:
    def __init__(self):
        with open("data/map/map.json") as fp:
            self.map = json.load(fp)
        

    def next_place(self, place, direction):
        for zone in self.map:
            if place in zone and direction in zone[place]:
                return zone[place][direction]

    def is_subplace(self, place, zone):
        for zone in self.map:
            if place in zone:
                return True
        
        return False
        
    
