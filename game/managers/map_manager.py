import json


class MapManager:
    def __init__(self):
        with open("data/map/map.json") as fp:
            self.map = json.load(fp)

    def next_place(self, place, direction):
        for _, zone in self.map.items():
            if place in zone and direction in zone[place]:
                return zone[place][direction]

    def is_subplace(self, place, zone):
        for _, zone in self.map.items():
            if place in zone:
                return True

        return False

    def list_places(self):
        places = []
        for zone_name, zone in self.map.items():
            places.append(zone_name)
            for place in zone:
                places.append(place)

        return places

    def list_directions(self):
        all_directions = set()
        for _, zone in self.map.items():
            for place, directions in zone.items():
                for direction in directions:
                    all_directions.add(direction)

        return all_directions
