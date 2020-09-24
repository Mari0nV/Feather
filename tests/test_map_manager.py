from feather.managers.map_manager import MapManager
import pytest


@pytest.mark.parametrize("place, direction, expected", [
    ["middle_forest", "north", "north_forest"],
    ["middle_forest", "south", "south_forest"],
    ["middle_forest", "west", "west_forest"],
    ["middle_forest", "east", "east_forest"]
])
def test_that_map_manager_returns_next_place(place, direction, expected):
    map_manager = MapManager()

    assert map_manager.next_place(place, direction) == expected


@pytest.mark.parametrize("subplace, zone, expected", [
    ["middle_forest", "forest", True],
    ["city_center", "forest", False],
    ["unknown_place", "forest", False],
    ["middle_forest", "unknown_zone", False],
])
def test_that_map_manager_detect_subplaces(
    subplace, zone, expected
):
    map_manager = MapManager()

    assert map_manager.is_subplace(subplace, zone) == expected
