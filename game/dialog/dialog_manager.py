
from game.dialog.dialog_mapping import dialog_mapping
from game.input_manager import InputManager
import json
import nltk
import random

class DialogManager(InputManager):
    def __init__(self, status_manager):
        with open('../data/dialog_dictionary.json', "r") as json_file:
            self.dialog_dictionary = json.load(json_file)

        self.status_manager = status_manager
        self.dialog_mapping = dialog_mapping
        InputManager.__init__(self)

    def detect_dialog(self, response):
        verbs = ["tell", "say", "speak", "explain", "declare", "order"]

        tokens = nltk.word_tokenize(response.lower())

        if len(tokens) == 0:
            return False

        if tokens[0] in verbs:
            return True 
        
        if tokens[0] in ["i", "you"] and len(tokens) > 1 and tokens[1] in verbs:
            return True
        
        return False
    
    def _is_interlocutor(self, word, tag=None):
        if word in ["him", "her", "spirit"]:
            return True
        
        if tag and tag in ["NP"]:
            return True
        
        return False
    
    def _skin_tokens(self, tokens, tags):
        # Remove player subject
        if tokens and tokens[0] in ["i", "you"]:
            tokens = tokens[1:]
            tags = tags[1:]
        
        # Remove a, an, the
        new_tags = []
        new_tokens = []
        for i, token in enumerate(tokens):
            if token not in ["a", "an", "the"]:
                new_tokens.append(token)
                new_tags.append(tags[i])
        
        return tokens, tags

    def _parse_tokens(self, tokens, tags):
        if len(tokens) in [0, 1]:
            return None

        if len(tokens) == 2:
            if tokens[1] in ["that", "to"] or \
                self._is_interlocutor(*tags[1]):
                return None
        
        # "Say to Mary..."
        if tokens[1] in ["to"] and self._is_interlocutor(*tags[2]):
            # "Say to Mary that..."
            if tokens[3] in ["that", "to"]:
                if len(tokens) >= 4:
                    return {
                        "interlocutor": tokens[2],
                        "tokens": tokens[4:]
                    }
                else:
                    return None
            # Say to Mary something...""
            else:
                return {
                        "interlocutor": tokens[2],
                        "tokens": tokens[3:]
                }
        
        # "Tell Bob..."
        if self._is_interlocutor(*tags[1]):
            # "Tell Bob that..."
            if tokens[2] in ["that", "to"]:
                return {
                    "interlocutor": tokens[1],
                    "tokens": tokens[3:]
                }
            # "Tell Bob something...
            else:
                return {
                    "interlocutor": tokens[1],
                    "tokens": tokens[2:]
                }

        # TODO Tell that something

        # "Say something to someone"
        if tokens[-2] in ["to"] and \
            self._is_interlocutor(*tags[-1]):
            return {
                "interlocutor": tokens[-1],
                "tokens": tokens[1:-2]
            }

        # "Say something"
        return {
            "interlocutor": None,
            "tokens": tokens[1:]
        }
    
    def process_response(self, response):
        tokens, tags = self._preprocess_response(response)
        skinned_tokens, skinned_tags = self._skin_tokens(tokens, tags)

        dialog_tokens = self._parse_tokens(skinned_tokens, skinned_tags)
        line = "".join(dialog_tokens["tokens"])
        interlocutor = dialog_tokens["interlocutor"]

        # TODO handle interlocutor

        result = None

        # check if line is in dictionary
        if not self.status_manager.is_alone():
            if line in self.dialog_dictionary:
                data = self.dialog_dictionary[line]
                if data in self.dialog_mapping:
                    result = self.dialog_mapping[data]
        
        # nobody_there = {(): {"msg": ["Nobody answers."]}}
        # return nobody_there, line, interlocutor

        # check status
        if result:
            for status, action in result.items():
                if status:
                    status_list = [status] if type(status) == str else list(status)
                    if self.status_manager.check_status(status_list):
                        self.do_action(action, line)
                        return
            if not status:
                self.do_action(action, line)
    
    def do_action(self, action, skinned_resp):
        if "msg" in action:
            print('\n', random.choice(action["msg"]).format(action=skinned_resp))
        if "update" in action:
            self.status_manager.update(action["update"])
        if "next" in action:
            self.process_response(action["next"])

