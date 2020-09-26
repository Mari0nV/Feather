import json

from feather.config import intro_file
from feather.managers.action_manager import ActionManager
from feather.managers.dialog_manager import DialogManager
from feather.managers.map_manager import MapManager
from feather.managers.move_manager import MoveManager
from feather.managers.output_manager import OutputManager
from feather.managers.status_manager import StatusManager


class GameManager:
    def __init__(self):
        self.map_manager = MapManager()
        self.status_manager = StatusManager(self.map_manager)
        self.output_manager = OutputManager()

        self.action_manager = ActionManager(self.status_manager, self.output_manager)
        self.dialog_manager = DialogManager(self.status_manager, self.output_manager)
        self.move_manager = MoveManager(
            self.status_manager, self.output_manager
        )

    def intro(self):
        with open(intro_file, "r") as fp:
            intro = json.load(fp)["intro"]
        self.output_manager.print(intro)

    def start(self):
        self.intro()
        response = input()
        while response.lower() != "quit":
            self.process_response(response)
            if self.status_manager.is_dead():
                break
            response = input()

    def process_response(self, response):
        # find response mapping in dialog or action dictionaries
        if self.dialog_manager.detect_dialog(response):
            self.dialog_manager.process_response(response)
        elif self.move_manager.detect_move(response):
            self.move_manager.process_response(response)
        else:
            self.action_manager.process_response(response)
