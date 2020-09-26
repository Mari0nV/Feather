import json

from feather.managers.action_manager import ActionManager


class MoveManager(ActionManager):
    def __init__(self, status_manager, output_manager, map_manager):
        with open("data/generated/move_dictionary.json") as fp:
            self.move_dictionary = json.load(fp)

        self.map_manager = map_manager
        self._cache = {}

        ActionManager.__init__(self, status_manager, output_manager)

    def detect_move(self, response):
        # check spelling and decompose response
        text, tags = self._preprocess_response(response)

        # remove subject, possessive, pronouns...
        clean_response = self._skin_response(text, tags)

        if clean_response not in self.action_dictionary:
            for key in self.move_dictionary:
                if clean_response.startswith(key):
                    self._cache[clean_response] = key
                    return True

        return False

    def _parse_destination(self, clean_response):
        if clean_response in self._cache:
            destination = clean_response.replace(
                self._cache[clean_response], ""
            ).strip()
        else:
            for key in self.move_dictionary:
                if clean_response.startswith(key):
                    destination = clean_response.replace(
                        self._cache[clean_response], ""
                    ).strip()

        if destination in self.map_manager.list_places():
            return destination
        elif destination in self.map_manager.list_directions():
            current_place = self.status_manager.get_current_place()
            return self.map_manager.next_place(current_place, destination)

    def retrieve_action(self, clean_response):
        destination = self._parse_destination(clean_response)

        if destination:
            with open(f"data/move/places/{destination}.json", "r") as fp:
                data = json.load(fp)

            if data:
                return self._choose_action_from_status(data, destination)
