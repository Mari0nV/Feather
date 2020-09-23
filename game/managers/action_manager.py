import json
import random

from game.managers.input_manager import InputManager


class ActionManager(InputManager):
    def __init__(self, status_manager, output_manager):
        with open("data/generated/action_dictionary.json") as json_file:
            self.action_dictionary = json.load(json_file)

        self.status_manager = status_manager
        self.output_manager = output_manager
        InputManager.__init__(self)

    def _skin_response(self, text, tags):
        # replacing some words
        for i, word in enumerate(text):
            if word in self.replacements:
                text[i] = self.replacements[word]
                tags[i] = (self.replacements[word], tags[i][1])

        skinned = ""
        # removing superfluous
        for word, word_type in tags:
            if word not in ["i", "my", "you", "your"] and word_type not in [
                "AT",
                "DET",
            ]:
                skinned += f"{word} "

        return skinned[:-1]

    def _choose_action_from_status(self, data, key):
        # check status and return action
        for status, action in data[key].items():
            if status and status != "default":
                if self.status_manager.check_status(status):
                    return action
        if not status or status == "default":
            return action

    def retrieve_action(self, skinned_response):
        # check if response is in dictionary
        if skinned_response in self.action_dictionary:
            key = self.action_dictionary[skinned_response]

            with open(f"data/action/{key}.json", "r") as fp:
                data = json.load(fp)

            if data:
                return self._choose_action_from_status(data, key)

    def process_response(self, response):
        # check spelling and decompose response
        text, tags = self._preprocess_response(response)

        # remove subject, possessive, pronouns...
        skinned_response = self._skin_response(text, tags)

        # retrieve action from dictionary and status checking
        action = self.retrieve_action(skinned_response)

        # perform choosen action
        if action:
            self.do_action(action, skinned_response)

    def do_action(self, action, skinned_resp):
        if "msg" in action:
            self.output_manager.print(
                random.choice(action["msg"]).format(action=skinned_resp)
            )
        if "update" in action:
            self.status_manager.update(action["update"])
        if "next" in action:
            self.process_response(action["next"])
