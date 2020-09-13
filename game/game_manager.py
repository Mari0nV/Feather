from game.forest_chapter.forest_chapter import ForestChapter
import json

class GameManager:
    def __init__(self):
        with open('../data/status.json') as json_file:
            self.all_status = json.load(json_file)["status"]
        with open('../data/dictionary.json') as json_file:
            self.dictionary = json.load(json_file)
        self.sequence = ForestChapter(self)
    
    def intro(self):
        print("You wake up in the middle of a forest, freezing as hell.")
        print("You see absolutely nothing in the dark, and you have no idea how you got here.\n")
        print("Is this a joke from university students? You're a freshman at the Strangeland university, and you were warned about hazing.\n")
        print("What is the first thing you do?")
    
    def load_sequence(self, chapter):
        self.sequence = chapter
    
    def start(self):
        self.intro()
        response = input()
        while response.lower() != "quit":
            self.sequence.process_response(response)
            response = input()

