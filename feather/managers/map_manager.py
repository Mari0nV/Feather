import json

from feather.config import map_file


class MapManager:
    def __init__(self):
        with open(map_file) as fp:
            self.map = json.load(fp)

    def alias_to_path(self, alias):
        for place_path, data in self.map.items():
            if alias in data["aliases"]:
                return place_path

    def next_place(self, place, direction):
        if direction in self.map[place]["directions"]:
            return self.map[place]["directions"][direction]

    def compute_distance(self, place, destination):
        pass
