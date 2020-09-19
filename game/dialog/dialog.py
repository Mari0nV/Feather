
from game.dialog.dialog_mapping import dialog_mapping
import json

class Dialog:
    def __init__(self, status):
        self.status = status
        self.dialog_mapping = dialog_mapping
        with open('../data/dialog_dictionary.json', "r") as json_file:
            self.dialog_dictionary = json.load(json_file)

    def detect_dialog(self, resp_tokens):
        verbs = ["tell", "say", "speak", "explain", "declare", "order"]

        if len(resp_tokens) == 0:
            return False

        if resp_tokens[0] in verbs:
            return True 
        
        if resp_tokens[0] in ["i", "you"] and len(resp_tokens) > 1 and resp_tokens[1] in verbs:
            return True
        
        return False
    
    def _is_interlocutor(self, word, tag=None):
        if word in ["him", "her", "spirit"]:
            return True
        
        if tag and tag in ["NP"]:
            return True
        
        return False
    
    def _skin_tokens(self, resp_tokens, tags):
        # Remove player subject
        if resp_tokens and resp_tokens[0] in ["i", "you"]:
            resp_tokens = resp_tokens[1:]
            tags = tags[1:]
        
        # Remove a, an, the
        new_tags = []
        new_tokens = []
        for i, token in enumerate(resp_tokens):
            if token not in ["a", "an", "the"]:
                new_tokens.append(token)
                new_tags.append(tags[i])
        
        return resp_tokens, tags

    def _parse_tokens(self, resp_tokens, tags):
        resp_tokens, tags = self._skin_tokens(resp_tokens, tags)

        if len(resp_tokens) in [0, 1]:
            return None

        if len(resp_tokens) == 2:
            if resp_tokens[1] in ["that", "to"] or \
                self._is_interlocutor(*tags[1]):
                return None
        
        # "Say to Mary..."
        if resp_tokens[1] in ["to"] and self._is_interlocutor(*tags[2]):
            # "Say to Mary that..."
            if resp_tokens[3] in ["that", "to"]:
                if len(resp_tokens) >= 4:
                    return {
                        "interlocutor": resp_tokens[2],
                        "tokens": resp_tokens[4:]
                    }
                else:
                    return None
            # Say to Mary something...""
            else:
                return {
                        "interlocutor": resp_tokens[2],
                        "tokens": resp_tokens[3:]
                }
        
        # "Tell Bob..."
        if self._is_interlocutor(*tags[1]):
            # "Tell Bob that..."
            if resp_tokens[2] in ["that", "to"]:
                return {
                    "interlocutor": resp_tokens[1],
                    "tokens": resp_tokens[3:]
                }
            # "Tell Bob something...
            else:
                return {
                    "interlocutor": resp_tokens[1],
                    "tokens": resp_tokens[2:]
                }

        # TODO Tell that something

        # "Say something to someone"
        if resp_tokens[-2] in ["to"] and \
            self._is_interlocutor(*tags[-1]):
            return {
                "interlocutor": resp_tokens[-1],
                "tokens": resp_tokens[1:-2]
            }

        # "Say something"
        return {
            "interlocutor": None,
            "tokens": resp_tokens[1:]
        }
    
    def find_mapping(self, resp_tokens, tags):
        tokens = self._parse_tokens(resp_tokens, tags)
        line = "".join(tokens["tokens"])
        interlocutor = tokens["interlocutor"]

        # TODO handle interlocutor

        # check if line is in dictionary
        if not self.status.is_alone():
            if line in self.dialog_dictionary:
                data = self.dialog_dictionary[line]
                if data in self.dialog_mapping:
                    return self.dialog_mapping[data], line
        
        nobody_there = {(): {"msg": ["Nobody answers."]}}
        return nobody_there, line


