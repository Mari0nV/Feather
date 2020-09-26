import pytest

from feather.managers.action_manager import ActionManager


@pytest.mark.parametrize("response, expected", [
    ["go to my univeristy", "go to university"],
    ["say, hi there!!!!", "say hi there"],
    ["i want an ice cream", "want ice cream"]
])
def test_that_action_manager_clean_responses(
    action_manager, response, expected
):
    assert action_manager._clean_response(response) == expected


def test_that_action_manager_process_response(
    action_manager
):
    action_manager.process_response("input action")

    assert action_manager.output_manager.history == [{
        "input": "input action",
        "outputs": ["msg output"]
    }]


def test_that_action_manager_retrieves_action(
    action_manager
):
    assert action_manager._retrieve_action("input action") == {
        "msg": ["msg output"]
    }
