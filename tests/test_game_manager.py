from feather.managers.game_manager import GameManager


def test_that_game_manager_outputs_intro():
    game_manager = GameManager()
    game_manager.intro()

    assert game_manager.output_manager.history == [
        {"output": "introduction"}
    ]


def test_that_game_manager_process_response():
    game_manager = GameManager()

    game_manager.process_response("input action")

    assert game_manager.output_manager.history == [
        {"input": "input action", "outputs": ["msg output"]}
    ]


def test_that_game_manager_starts_and_quits_game(mocker):
    mocker.patch("builtins.input", mocker.Mock(side_effect=["input action", "quit"]))
    game_manager = GameManager()

    game_manager.start()

    assert game_manager.output_manager.history == [
        {"output": "introduction"},
        {"input": "input action", "outputs": ["msg output"]}
    ]
