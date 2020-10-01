import json

from feather.config import (
    map_dictionary_file,
    map_file
)

class MapManager:
    def __init__(self):
        with open(map_file) as fp:
            self.map = json.load(fp)

        with open(map_dictionary_file) as fp:
            self.map_dictionary = json.load(fp)

    def alias_to_path(self, alias):
        if alias in self.map_dictionary:
            # TODO Handle multiple paths for one alias
            return self.map_dictionary[alias][0]

    def next_place(self, place, direction):
        if direction in self.map[place]["directions"]:
            return self.map[place]["directions"][direction]

    def compute_distance(self, place, destination):
        pass
