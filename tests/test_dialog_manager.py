import pytest


@pytest.mark.parametrize("input, expected", [
    ["say hello to Wendy", True],
    ["say hi!", True],
    # ["\"Where are you going?\"", True],  # TODO Handle this case
    ["- I didn't know.", True],
    ["say", False],
    ["say that", False],
])
def test_that_dialog_manager_detects_dialog(dialog_manager, input, expected):
    assert dialog_manager.detect_dialog(input) == expected
