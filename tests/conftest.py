import os
import pytest

os.environ["FEATHER_STATUS_FILE"] = "tests/fake_data/fake_status.json"
os.environ["FEATHER_MAP_FILE"] = "tests/fake_data/fake_map.json"
os.environ["FEATHER_SPEECH_PATH"] = "tests/fake_data/fake_speech"
os.environ["FEATHER_DIALOG_COMBINATIONS_FILE"] = "tests/fake_data/fake_dialog_combinations.json"
os.environ["FEATHER_REPLACEMENTS_FILE"] = "tests/fake_data/replacements.json"

from feather.managers.dialog_manager import DialogManager
from feather.managers.map_manager import MapManager
from feather.managers.status_manager import StatusManager



class FakeOutputManager:
    def print(text):
        return text


@pytest.fixture
def dialog_manager():
    status_manager = StatusManager(
        MapManager()
    )
    return DialogManager(
        status_manager,
        FakeOutputManager())