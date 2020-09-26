import pytest


@pytest.mark.parametrize("response,detected", [
    ["go north", True],
    ["go to university", True],
    ["climb tree", False]
])
def test_that_move_manager_detects_move(
    move_manager, response, detected):
    assert move_manager.detect_move(response) == detected


@pytest.mark.parametrize("response, cache", [
    ["go west", {}], 
    ["go west", {"go west": "go"}],
    ["go to west_forest", {}]
])
def test_that_move_manager_parses_destination(
    move_manager, response, cache):
    move_manager.cache = cache

    assert move_manager._parse_destination(response) == "west_forest"


def test_that_move_manager_retrieves_action(
    move_manager):
    assert move_manager._retrieve_action("go west") == {
        "msg": ["you go to west_forest"]
    }
