from game.managers.action_manager import ActionManager
from nltk import word_tokenize

class MoveManager(ActionManager):
    def __init__(self, status_manager):
        ActionManager.__init__(status_manager)
    
    def detect_move(self, response):
        tokens = word_tokenize(response.lower())