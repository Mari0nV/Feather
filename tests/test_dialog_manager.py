import pytest


@pytest.mark.parametrize("input, expected", [
    ["say hello to Wendy", True],
    ["say hi!", True],
    # ["\"Where are you going?\"", True],  # TODO Handle this case
    ["- I didn't know.", True],
    ["say", False],
])
def test_that_dialog_manager_detects_dialog(dialog_manager, input, expected):
    assert dialog_manager.detect_dialog(input) == expected


choices = { "results": {
        "place.middle_forest, presence.friend": {
            "msg": ["place.middle_forest, presence.friend"]
        },
        "presence.other_friend": {
            "msg": ["presence.other_friend"]
        },
        "default": {
            "msg": ["default"]
        }
    }}


@pytest.mark.parametrize("interlocutor_status, friend_presence, expected", [
    ["presence.friend", True, "place.middle_forest, presence.friend"],
    ["", True, "place.middle_forest, presence.friend"],
    ["presence.friend", False, "default"],
    ["", False, "default"],
])
def test_dialog_managers_chooses_action_from_status(
    dialog_manager, interlocutor_status, friend_presence, expected):

    dialog_manager.status_manager.status["presence"]["friend"] = friend_presence
    assert dialog_manager._choose_action_from_status(
        choices, interlocutor_status)["msg"][0] == expected


@pytest.mark.parametrize("response, expected", [
    ["say hello to Wendy", ("Wendy", "hello")],
    ["say hello", (None, "hello")]
])
def test_that_dialog_manager_parses_dialog(
    dialog_manager, response, expected):

    assert dialog_manager._parse_dialog(response) == expected


@pytest.mark.parametrize("speech, presence, cache, expected", [
    ["say hello to Wendy", True, {}, "hello, says Wendy."],
    ["say hello to Wendy", True, 
        {"say hello to Wendy": {"interlocutor": "Wendy", "speech": "hello"}},
        "hello, says Wendy."],
    ["say hello", True, {}, "hello, says Wendy."],
    ["say hello", False, {}, "nobody answers you."],
    ["say hello", True, 
        {"say hello": {"speech": "hello"}},
        "hello, says Wendy."],
    ["say hello to Bob", True, {},
        "nobody answers you."],
])
def test_that_dialog_manager_retrieves_action(
    dialog_manager, speech, presence, cache, expected):
    dialog_manager.status_manager["presence"]["wendy"] = presence
    dialog_manager._cache = cache

    assert dialog_manager._retrieve_action(
        speech
    )["msg"][0] == expected
