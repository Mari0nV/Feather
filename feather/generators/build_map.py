import json
import os


def _compute_directions(json_file, place, coordinates):
    with open(json_file, "r") as fp:
        content = json.load(fp)

    directions = {}

    splitted = place.split('.')
    place_path = '.'.join(splitted[:-1])

    if "map" in content:
        x, y = coordinates
        if x > 0:
            directions["north"] = f"{place_path}.{content['map'][x-1][y]}" \
                if place_path else content['map'][x-1][y]
        if x < len(content["map"]) - 1:
            directions["south"] = f"{place_path}.{content['map'][x+1][y]}" \
                if place_path else content['map'][x+1][y]
        if y > 0:
            directions["west"] = f"{place_path}.{content['map'][x][y-1]}" \
                if place_path else content['map'][x][y-1]
        if y < len(content["map"][0]) - 1:
            directions["east"] = f"{place_path}.{content['map'][x][y+1]}" \
                if place_path else content['map'][x][y+1]

    if "borders" in content and splitted[-1] in content["borders"]:
        for direction, destination in content["borders"][splitted[-1]].items():
            if '.' not in destination and place_path != '':
                directions[direction] = f"{place_path}.{destination}"
            else:
                directions[direction] = destination
    
    # TODO if directions are missing, look to upper map

    return directions


def _build_map_path(map_paths, file_path, parent=None):
    with open(file_path, "r") as fp:
        world_map = json.load(fp)

    if "map" not in world_map:
        return

    subdirs = os.listdir(os.path.dirname(file_path))
    for x, row in enumerate(world_map["map"]):
        for y, place in enumerate(row):
            new_parent = ".".join([parent, place]) if parent else place

            if place in subdirs:
                new_file_path = f"{os.path.dirname(file_path)}/{place}/{place}_map.json"
                _build_map_path(map_paths, new_file_path, new_parent)

            map_paths[new_parent] = {
                "directions": _compute_directions(file_path, new_parent, (x, y)),
                "aliases": world_map["aliases"][place]
                    if "aliases" in world_map and place in world_map["aliases"] else []
            }


def build_map_paths(json_file, filename):
    map_paths = {}
    _build_map_path(map_paths, json_file)

    with open(f"data/generated/{filename}.json", "w+") as fd:
        json.dump(map_paths, fd)
