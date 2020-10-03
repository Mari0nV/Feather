import json

from feather.generators.build_map import build_map_data


def test_that_generators_build_map_data(mocker):
    build_map_data.__globals__[
        "generated_map_aliases_file"] = "tests/mock_data/generated/map_aliases.json"
    build_map_data.__globals__[
        "generated_map_file"] = "tests/mock_data/generated/map.json"

    build_map_data()

    with open("tests/mock_data/generated/map_aliases.json", "r") as fp:
        aliases = json.load(fp)

    assert aliases == {
        "dorms": ["university.dorms"],
        "dormitories": ["university.dorms"],
        "gymnasium": ["university.gymnasium"],
        "gym": ["university.gymnasium"]
    }

    with open("tests/mock_data/generated/map.json", "r") as fp:
        global_map = json.load(fp)

    assert global_map == {
        "university.dorms.men_dorms": {
            "directions": {
                "east": "university.dorms.women_dorms"
            }
        },
        "university.dorms.women_dorms": {
            "directions": {
                "west": "university.dorms.men_dorms"
            }
        },
        "university.dorms": {
            "directions": {
                "south": "university.science_building",
                "east": "university.gymnasium",
                "north": "university.science_building"
            },
            "aliases": [
                "dorms",
                "dormitories"
            ]
        },
        "university.gymnasium": {
            "directions": {
                "south": "university.cafet",
                "west": "university.dorms",
                "east": "forest.cemetery"
            },
            "aliases": [
                "gymnasium",
                "gym"
            ]
        },
        "university.science_building": {
            "directions": {
                "north": "university.dorms",
                "east": "university.cafet"
            }
        },
        "university.cafet": {
            "directions": {
                "north": "university.gymnasium",
                "west": "university.science_building",
                "east": "forest.middle_forest"
            }
        },
        "university": {
            "directions": {
                "east": "forest"
            }
        },
        "forest.cemetery.cemetery_north": {
            "directions": {
                "south": "forest.cemetery.cemetery_south"
            }
        },
        "forest.cemetery.cemetery_south": {
            "directions": {
                "north": "forest.cemetery.cemetery_north"
            }
        },
        "forest.cemetery": {
            "directions": {
                "south": "forest.middle_forest",
                "east": "forest.north_west_forest"
            }
        },
        "forest.north_west_forest": {
            "directions": {
                "south": "forest.west_forest",
                "west": "forest.cemetery"
            }
        },
        "forest.middle_forest": {
            "directions": {
                "north": "forest.cemetery",
                "east": "forest.west_forest"
            }
        },
        "forest.west_forest": {
            "directions": {
                "north": "forest.north_west_forest",
                "west": "forest.middle_forest"
            }
        },
        "forest": {
            "directions": {
                "west": "university"
            }
        }
    }