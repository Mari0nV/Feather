import json
import os

from feather.config import (
    generated_map_aliases_file,
    generated_map_file,
    map_path
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

    def check_event(self, place, day, hours=None):
        path = f"{map_path}/{place.replace('.', '/')}/{place.split('.')[-1]}_map.json"
        if os.path.exists(path):
            with open(path, "r") as fp:
                content = json.load(fp)

            if "presence" in content:
                for date in content["presence"].keys():
                    range_days = date.split('-')
                    first_day = int(range_days[0].replace("DAY", ""))
                    last_day = int(range_days[1].replace("DAY", "")) \
                        if len(range_days) > 1 else first_day

                    if day in range(first_day, last_day + 1):
                        yield ("presence", content["presence"][date])
