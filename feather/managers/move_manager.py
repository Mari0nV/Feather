import json

from feather.config import (
    move_combinations_file,
    places_path
)
from feather.managers.action_manager import ActionManager


class MoveManager(ActionManager):
    def __init__(self, status_manager, output_manager):
        with open(move_combinations_file, "r") as fp:
            self.move_combinations = json.load(fp)["combinations"]

        self.map_manager = status_manager.map_manager
        self._cache = {}

        ActionManager.__init__(self, status_manager, output_manager)

    def detect_move(self, response):
        # check spelling and replace or remove words
        clean_response = self._clean_response(response)

        self._look_for_key(clean_response)

        if clean_response in self._cache:
            return True        

        return False
    
    def _look_for_key(self, clean_response):
        if clean_response not in self.action_dictionary:
            for key in self.move_combinations:
                if clean_response.startswith(key):
                    if clean_response not in self._cache or self._cache[clean_response] < key:
                        self._cache[clean_response] = key

    def _parse_destination(self, clean_response):
        if clean_response not in self._cache:
            self._look_for_key(clean_response)

        destination = clean_response.replace(
                self._cache[clean_response], ""
            ).strip()

        place_path = self.map_manager.alias_to_path(destination)
        if not place_path:
            # We make the assumption that destination is a direction
            current_place = self.status_manager.get_current_place()
            place_path = self.map_manager.next_place(current_place, destination)

        return place_path

    def _retrieve_action(self, clean_response):
        destination = self._parse_destination(clean_response)

        if destination:
            with open(f"{places_path}/{destination.replace('.', '/')}.json", "r") as fp:
                data = json.load(fp)

            if data:
                return self._choose_action_from_status(data)
