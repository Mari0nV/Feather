import nltk
import os
import pytest
import shutil

os.environ["FEATHER_INTRO_FILE"] = "tests/mock_data/intro.json"
os.environ["FEATHER_STATUS_FILE"] = "tests/mock_data/status.json"
os.environ["FEATHER_REPLACEMENTS_FILE"] = "tests/mock_data/replacements.json"
os.environ["FEATHER_MOVE_COMBINATIONS_FILE"] = "tests/mock_data/move_combinations.json"
os.environ["FEATHER_DIALOG_COMBINATIONS_FILE"] = "tests/mock_data/dialog_combinations.json"

generated_path = "tests/mock_data/generated"
os.environ["FEATHER_GENERATED_PATH"] = generated_path
os.environ["FEATHER_GENERATED_MAP_FILE"] = "tests/mock_data/manually_generated/map.json"
os.environ[
    "FEATHER_GENERATED_MAP_ALIASES_FILE"] = "tests/mock_data/manually_generated/map_aliases.json"
os.environ[
    "FEATHER_GENERATED_MOVE_COMBINATIONS_FILE"] = "tests/mock_data/manually_generated/move_combinations.json"
os.environ[
    "FEATHER_GENERATED_DIALOG_COMBINATIONS_FILE"] = "tests/mock_data/manually_generated/dialog_combinations.json"
os.environ[
    "FEATHER_GENERATED_ACTION_FILE"] = "tests/mock_data/manually_generated/actions.json"
os.environ[
    "FEATHER_GENERATED_DIALOG_FILE"] = "tests/mock_data/manually_generated/dialogs.json"
os.environ[
    "FEATHER_GENERATED_REPLACEMENTS_FILE"] = "tests/mock_data/manually_generated/replacements.json"

os.environ["FEATHER_SPEECH_PATH"] = "tests/mock_data/speech"
os.environ["FEATHER_ACTION_PATH"] = "tests/mock_data/action"
os.environ["FEATHER_PLACES_PATH"] = "tests/mock_data/move"
os.environ["FEATHER_MAP_PATH"] = "tests/mock_data/map"


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


@pytest.yield_fixture
def generated_folder():
    if not os.path.exists(generated_path):
        os.mkdir(generated_path)
    yield
    shutil.rmtree(generated_path)
