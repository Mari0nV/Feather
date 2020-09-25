import json

from feather.config import (
    dialog_combinations_file,
    speech_path
)
from feather.managers.input_manager import InputManager
from feather.utils.utils import choose_best_decomposition


class DialogManager(InputManager):
    def __init__(self, status_manager, output_manager):
        with open(dialog_combinations_file, "r") as json_file:
            self.dialog_combinations = json.load(json_file)["combinations"]

        self.status_manager = status_manager
        self.output_manager = output_manager

        self._cache = {}

        InputManager.__init__(self)
    
    def detect_dialog(self, response):
        # check spelling and decompose response
        text, tags = self._preprocess_response(response)

        # remove subject, possessive, pronouns...
        skinned_response = self._skin_response(text, tags)

        parsing = choose_best_decomposition(skinned_response, self.dialog_combinations)

        if parsing:
            self._cache = {
                "skinned_response": skinned_response,
                "parsing": parsing
            }
            return True

        self._cache = {}
        return False

    def _parse_dialog(self, skinned_response):
        parsing = choose_best_decomposition(skinned_response, self.dialog_combinations)

        interlocutor = parsing["interlocutor"] if "interlocutor" in parsing else None
        speech = parsing["speech"]

        return interlocutor, speech

    def _choose_action_from_status(self, choices, key, interlocutor_status):
        # check status and return action
        for status, action in choices[key].items():
            if status and status != "default":
                if interlocutor_status in status and self.status_manager.check_status(status):
                    return action
        if not status or status == "default":
            return action

    def _retrieve_action(self, skinned_response):
        if not self._cache:
            interlocutor, speech = self._parse_dialog(skinned_response)
        else:
            interlocutor = self._cache["parsing"]["interlocutor"]
            speech = self._cache["parsing"]["speech"]

            interlocutor_status = f"presence.{interlocutor.lower()}" if interlocutor else ""
        
        with open(f"{speech_path}/{speech}", "r") as json_file:
            choices = json.load(json_file)
        
        if choices:
            return self._choose_action_from_status(choices, speech, interlocutor_status)
