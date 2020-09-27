import pytest

from feather.managers.game_manager import GameManager


def test_that_game_manager_outputs_intro():
    game_manager = GameManager()
    game_manager.intro()

    assert game_manager.output_manager.history == [
        {"output": "introduction"}
    ]


@pytest.mark.parametrize("user_input, history", [
    ["input action", {"input": "input action", "outputs": ["msg output"]}],
    ["say hello", {"input": "say hello", "outputs": ["nobody answers you."]}]
])
def test_that_game_manager_process_response(
    user_input, history
):
    game_manager = GameManager()

    game_manager.process_response(user_input)

    assert game_manager.output_manager.history[0] == history


def test_that_game_manager_starts_and_quits_game(mocker):
    mocker.patch("builtins.input", mocker.Mock(side_effect=["input action", "quit"]))
    game_manager = GameManager()

    game_manager.start()

    assert game_manager.output_manager.history == [
        {"output": "introduction"},
        {"input": "input action", "outputs": ["msg output"]}
    ]
