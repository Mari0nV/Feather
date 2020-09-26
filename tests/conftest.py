import nltk
import os
import pytest

os.environ["FEATHER_INTRO_FILE"] = "tests/fake_data/fake_intro.json"
os.environ["FEATHER_STATUS_FILE"] = "tests/fake_data/fake_status.json"
os.environ["FEATHER_MAP_FILE"] = "tests/fake_data/fake_map.json"
os.environ["FEATHER_ACTION_DICTIONARY_FILE"] = "tests/fake_data/fake_action_dictionary.json"
os.environ["FEATHER_SPEECH_PATH"] = "tests/fake_data/fake_speech"
os.environ["FEATHER_ACTION_PATH"] = "tests/fake_data/fake_action"
os.environ["FEATHER_PLACES_PATH"] = "tests/fake_data/fake_move"
os.environ["FEATHER_MOVE_COMBINATIONS_FILE"] = "tests/fake_data/fake_move_combinations.json"
os.environ["FEATHER_DIALOG_COMBINATIONS_FILE"] = "tests/fake_data/fake_dialog_combinations.json"
os.environ["FEATHER_REPLACEMENTS_FILE"] = "tests/fake_data/fake_replacements.json"

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