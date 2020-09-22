from game.managers.action_manager import ActionManager
from game.managers.dialog_manager import DialogManager
from game.managers.status_manager import StatusManager
from game.managers.output_manager import OutputManager

import json


class GameManager:
    def __init__(self):

        self.status_manager = StatusManager()
        self.output_manager = OutputManager()
        self.dialog_manager = DialogManager(self.status_manager, self.output_manager)
        self.action_manager = ActionManager(self.status_manager, self.output_manager)
    
    def intro(self):
        with open("data/intro.json", "r") as fp:
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
        else:
            self.action_manager.process_response(response)
