import json

from feather.config import (
    generated_map_aliases_file,
    generated_map_file
)


class MapManager:
    def __init__(self):
        with open(generated_map_file) as fp:
            self.map = json.load(fp)

        with open(generated_map_aliases_file) as fp:
            self.map_aliases = json.load(fp)

    def alias_to_path(self, alias):
        if alias in self.map_aliases:
            # TODO Handle multiple paths for one alias
            return self.map_aliases[alias][0]

    def next_place(self, place, direction):
        if direction in self.map[place]["directions"]:
            return self.map[place]["directions"][direction]

    def compute_distance(self, place, destination):
        pass
