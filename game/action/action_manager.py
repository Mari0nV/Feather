from game.action.generic_mapping import generic_mapping
from game.input_manager import InputManager
import random
import json

class ActionManager(InputManager):
    def __init__(self, status_manager):
        with open('../data/action_dictionary.json') as json_file:
            self.action_dictionary = json.load(json_file)
        
        self.status_manager = status_manager
        self.generic_mapping = generic_mapping
        InputManager.__init__(self)

    def _skin_response(self, text, tags):
        # replacing some words
        for i, word in enumerate(text):
            if word in self.replacements:
                text[i] = self.replacements[word]

        skinned = ""
        # removing superfluous
        for word, word_type in tags:
            if word not in ["i", "my", "you", "your"] and word_type not in ["AT", "DET"]:
                skinned += f"{word} "

        return skinned[:-1]
    
    def process_response(self, response, mapping):
        # check spelling and decompose response
        text, tags = self._preprocess_response(response)

        # remove subject, possessive, pronouns...
        skinned_response = self._skin_response(text, tags)
        result = None

        # check if response is in dictionary
        if skinned_response in self.action_dictionary:
            data = self.action_dictionary[skinned_response]
            if data in mapping:
                result = mapping[data]
            elif data in self.generic_mapping:
                result = self.generic_mapping[data]
        elif skinned_response in self.internal_mapping:
            result = self.internal_mapping[skinned_response]
        else:
            ...
            # nlp_response = self.nlp(skinned_response)
            # best_sim = {
            #     "similarity": 0,
            #     "expression": None,
            #     "mapping": None
            # }
            # 
            #     for key in mapping:
            #         sim = nlp_response.similarity(self.nlp(key))
            #         if sim > best_sim["similarity"]:
            #             best_sim.update(similarity=sim, expression=key, mapping=mapping)
            # return best_sim["mapping"][best_sim["expression"]]

        # check status
        if result:
            for status, action in result.items():
                if status:
                    status_list = [status] if type(status) == str else list(status)
                    if self.status_manager.check_status(status_list):
                        self.do_action(action, skinned_response, mapping)
                        return
            if not status:
                self.do_action(action, skinned_response, mapping)
    
    def do_action(self, action, skinned_resp, mapping):
        if "msg" in action:
            print('\n', random.choice(action["msg"]).format(action=skinned_resp))
        if "update" in action:
            self.status_manager.update(action["update"])
        if "next" in action:
            self.process_response(action["next"], mapping)
