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

        self._cache = {}

        InputManager.__init__(self, output_manager)
    
    def _update_cache(self, clean_response, parsing):
        self._cache = {} if len(self._cache) > 100 else self._cache
        self._cache[clean_response] = parsing
    
    def detect_dialog(self, response):
        # check spelling and replace or remove words
        clean_response = self._clean_response(response)

        parsing = choose_best_decomposition(clean_response, self.dialog_combinations)

        if parsing:
            self._update_cache(clean_response, parsing)
            return True

        return False

    def _parse_dialog(self, clean_response):
        parsing = choose_best_decomposition(clean_response, self.dialog_combinations)

        interlocutor = parsing["interlocutor"] if "interlocutor" in parsing else None
        speech = parsing["speech"]

        return interlocutor, speech

    def _choose_action_from_status(self, choices, interlocutor_status):
        # check status and return action
        for status, action in choices["results"].items():
            if status and status != "default":
                if interlocutor_status in status and self.status_manager.check_status(status):
                    return action
        if not status or status == "default":
            return action

    def _retrieve_action(self, clean_response):
        if clean_response in self._cache:
            interlocutor = self._cache[clean_response]["interlocutor"]
            speech = self._cache[clean_response]["speech"]
        else:
            interlocutor, speech = self._parse_dialog(clean_response)

        interlocutor_status = f"presence.{interlocutor.lower()}" if interlocutor else ""
        
        with open(f"{speech_path}/{speech}.json", "r") as json_file:
            choices = json.load(json_file)
        
        if choices:
            return self._choose_action_from_status(choices, interlocutor_status)
