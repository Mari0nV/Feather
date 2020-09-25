import json

from feather.config import (
    dialog_combinations_file,
    speech_file
)
from feather.managers.input_manager import InputManager
from feather.utils.utils import choose_best_decomposition


class DialogManager(InputManager):
    def __init__(self, status_manager, output_manager):
        with open(speech_file, "r") as json_file:
            self.speech_dictionary = json.load(json_file)
        with open(dialog_combinations_file, "r") as json_file:
            self.dialog_combinations = json.load(json_file)

        self.status_manager = status_manager
        self.output_manager = output_manager

        self._cache = {}

        InputManager.__init__(self)

    def _parse_dialog(self, skinned_response):
        parsing = choose_best_decomposition(skinned_response)

        interlocutor = parsing["interlocutor"] if "interlocutor" in parsing else None
        speech = parsing["speech"]

        return interlocutor, speech

    def detect_dialog(self, response):
        skinned_response = self._skin_response()
        parsing = choose_best_decomposition(skinned_response)

        if parsing:
            self._cache = {
                "skinned_response": skinned_response,
                "parsing": parsing
            }
            return True

        self._cache = {}
        return False

    def _skin_response(self, tokens, tags):
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

    def _retrieve_action(self, skinned_response):
        interlocutor, speech = self._parse_dialog(skinned_response)

        # # check if line is in dictionary
        # if not self.status_manager.is_alone():
        #     if line in self.speech_dictionary:
        #         result = self.speech_dictionary[line]
        #         # if data in self.dialog_mapping:
        #         #     result = self.dialog_mapping[data]
        # else:
        #     result = {(): {"msg": ["Nobody answers."]}}

        # # check status
        # if result:
        #     for status, action in result.items():
        #         if status:
        #             if self.status_manager.check_status(status):
        #                 self.do_action(action, line)
        #                 return
        #     if not status:
        #         self.do_action(action, line)
        # else:
        #     presence = self.status_manager.get_presence()
        #     # if presence[0] in self.dialog_default_mapping:
        #     #     action = self.dialog_default_mapping[presence[0]]
        #     #     self.do_action(action, line)
