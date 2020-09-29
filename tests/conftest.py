import nltk
import os
import pytest

os.environ["FEATHER_INTRO_FILE"] = "tests/mock_data/intro.json"
os.environ["FEATHER_STATUS_FILE"] = "tests/mock_data/status.json"
os.environ["FEATHER_MAP_FILE"] = "tests/mock_data/map.json"
os.environ["FEATHER_ACTION_DICTIONARY_FILE"] = "tests/mock_data/action_dictionary.json"
os.environ["FEATHER_SPEECH_PATH"] = "tests/mock_data/speech"
os.environ["FEATHER_ACTION_PATH"] = "tests/mock_data/action"
os.environ["FEATHER_PLACES_PATH"] = "tests/mock_data/move"
os.environ["FEATHER_MOVE_COMBINATIONS_FILE"] = "tests/mock_data/move_combinations.json"
os.environ["FEATHER_DIALOG_COMBINATIONS_FILE"] = "tests/mock_data/dialog_combinations.json"
os.environ["FEATHER_REPLACEMENTS_FILE"] = "tests/mock_data/replacements.json"

from feather.managers.action_manager import ActionManager
from feather.managers.dialog_manager import DialogManager
from feather.managers.map_manager import MapManager
from feather.managers.move_manager import MoveManager
from feather.managers.output_manager import OutputManager
from feather.managers.status_manager import StatusManager


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


@pytest.fixture
def dialog_manager():
    status_manager = StatusManager(
        MapManager()
    )
    output_manager = OutputManager()
    return DialogManager(
        status_manager,
        output_manager)


@pytest.fixture
def action_manager():
    status_manager = StatusManager(
        MapManager()
    )
    output_manager = OutputManager()
    return ActionManager(
        status_manager,
        output_manager)


@pytest.fixture
def move_manager():
    status_manager = StatusManager(
        MapManager()
    )
    output_manager = OutputManager()
    return MoveManager(
        status_manager,
        output_manager)