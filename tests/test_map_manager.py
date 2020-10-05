from feather.managers.map_manager import MapManager
import pytest


@pytest.mark.parametrize("place, direction, expected", [
    ["forest.middle_forest", "north", "forest.north_forest"],
    ["forest.middle_forest", "south", "forest.south_forest"],
    ["forest.middle_forest", "west", "forest.west_forest"],
    ["forest.middle_forest", "east", "forest.east_forest"]
])
def test_that_map_manager_returns_next_place(place, direction, expected):
    map_manager = MapManager()

    assert map_manager.next_place(place, direction) == expected


@pytest.mark.parametrize("alias,path", [
    ["west forest", "forest.west_forest"],
    ["woods", "forest"]
])
def test_that_map_manager_converts_alias_to_path(
    alias, path
):
    map_manager = MapManager()

    assert map_manager.alias_to_path(alias) == path


def test_that_map_manager_checks_events():
    map_manager = MapManager()

    check_event = map_manager.check_event("forest.river", day=1)

    assert next(check_event) == ("presence", ["Samuel"])
    assert next(check_event) == ("presence", ["Bob"])

    no_event = map_manager.check_event("forest.river", day=8)

    with pytest.raises(StopIteration):
        next(no_event)
