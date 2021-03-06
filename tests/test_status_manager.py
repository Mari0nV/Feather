import pytest

from feather.managers.map_manager import MapManager
from feather.managers.status_manager import StatusManager


@pytest.mark.parametrize("status,expected", [
    ["place:forest.middle_forest", True],
    ["!place:forest.middle_forest", False],
    ["place:forest.east_forest", False],
    ["!place:forest.east_forest", True],
    ["!mental_state:tired", False],
    ["mental_state:unknown", False],
    ["mental_state:tired, active:gps", False],
    ["mental_state:tired, !active:gps", True],
    ["mental_state:tired, !place:forest.north_forest", True],
])
def test_that_status_are_checked(status, expected):
    status_manager = StatusManager(MapManager())

    assert status_manager.check_status(status) == expected


def test_that_status_are_updated():
    status_manager = StatusManager(MapManager())

    update = {
        "place:forest.south_forest": True,
        "mental_state:happy": True,
        "mental_state:tired": False,
        "duration": 0.5
    }

    status_manager.update(update)

    assert status_manager.status["place"] == "forest.south_forest"
    assert status_manager.status["mental_state"]["happy"]
    assert not status_manager.status["mental_state"]["tired"]
    assert status_manager.status["day"] == 1.5


def test_that_status_manager_checks_whether_player_is_alone():
    status_manager = StatusManager(MapManager())

    assert status_manager.is_alone()

    status_manager.update({"presence:friend": True})

    assert not status_manager.is_alone()


def test_that_status_manager_checks_whether_player_is_dead():
    status_manager = StatusManager(MapManager())

    assert not status_manager.is_dead()

    status_manager.update({"physical_state:dead": True})

    assert status_manager.is_dead()


def test_that_status_manager_gets_presence():
    status_manager = StatusManager(MapManager())

    assert status_manager.get_presence() == []

    status_manager.update({
        "presence:friend1": True,
        "presence:friend2": True
        })

    assert status_manager.get_presence() == [
        "friend1",
        "friend2"
    ]


def test_that_status_manager_gets_current_place():
    status_manager = StatusManager(MapManager())

    assert status_manager.get_current_place() == "forest.middle_forest"


def test_that_status_manager_acts_like_status_list():
    status_manager = StatusManager(MapManager())

    assert len(status_manager) == len(status_manager.status)
    assert status_manager["place"] == status_manager.status["place"]


@pytest.mark.parametrize("place, status, expected", [
    ["forest", "forest", True],
    ["forest.cemetery", "forest.cemetery", True],
    ["forest.cemetery.north", "forest.cemetery", True],
    ["forest.cemetery", "forest", True],
    ["forest.cemetery", "forest.river", False],
])
def test_that_status_managers_detects_nested_places(
    place, status, expected
):
    status_manager = StatusManager(MapManager())
    status_manager.status["place"] = place

    assert status_manager._is_in_place(status) == expected
