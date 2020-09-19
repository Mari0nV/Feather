from game.chapters.forest_chapter.forest_chapter import ForestChapter
from game.status import Status
from game.dialog.dialog import Dialog
import json
import time

class GameManager:
    def __init__(self):
        with open('../data/action_dictionary.json') as json_file:
            self.dictionary = json.load(json_file)
        with open("../data/replacements.json") as json_file:
            self.replacements = json.load(json_file)

        self.status = Status()
        self.dialog = Dialog(self.status)
        self.sequence = ForestChapter(self)
    
    def intro(self):
        print("You wake up in the middle of a forest, freezing as hell." \
              " You see absolutely nothing in the dark, and you have no idea how you got here." \
              " Is this a joke from university students? You're a freshman at the Strangeland university, and you were warned about hazing." \
              " What is the first thing you do?")
    
    def load_sequence(self, chapter):
        self.sequence = chapter

    def start(self):
        self.intro()
        print()
        response = input()
        while response.lower() != "quit":
            self.sequence.process_response(response)
            if "dead" in self.status["physical_state"]:
                break
            response = input()

