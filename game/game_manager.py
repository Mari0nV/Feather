from game.chapters.forest_chapter.forest_chapter import ForestChapter
from game.status_manager import StatusManager
from game.dialog.dialog_manager import DialogManager
from game.action.action_manager import ActionManager


class GameManager:
    def __init__(self):

        self.status_manager = StatusManager()
        self.dialog_manager = DialogManager(self.status_manager)
        self.action_manager = ActionManager(self.status_manager)

        self.load_chapter(ForestChapter)
    
    def intro(self):
        print("You wake up in the middle of a forest, freezing as hell." \
              " You see absolutely nothing in the dark, and you have no idea how you got here." \
              " Is this a joke from university students? You're a freshman at the Strangeland university, and you were warned about hazing." \
              " What is the first thing you do?")
    
    def load_chapter(self, chapter):
        self.chapter = chapter()

    def start(self):
        self.intro()
        print()
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
            self.action_manager.process_response(response, self.chapter.mapping)
