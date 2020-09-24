import pytest

from feather.managers.map_manager import MapManager
from feather.managers.status_manager import StatusManager


@pytest.mark.parametrize("status,expected", [
    ["place.middle_forest", True],
    ["!place.middle_forest", False],
    ["place.east_forest", False],
    ["!place.east_forest", True],
    ["mental_state.tired, active.gps", False],
    ["mental_state.tired, !active.gps", True],
    ["mental_state.tired, !place.north_forest", True],
])
def test_that_status_are_checked(status, expected):
    status_manager = StatusManager(MapManager())

    assert status_manager.check_status(status) == expected


def test_that_status_are_updated():
    status_manager = StatusManager(MapManager())

    update = {
        "place.south_forest": True,
        "mental_state.happy": True,
        "mental_state.tired": False
    }

    status_manager.update(update)

    assert status_manager.status["place"] == "south_forest"
    assert status_manager.status["mental_state"]["happy"]
    assert not status_manager.status["mental_state"]["tired"]
