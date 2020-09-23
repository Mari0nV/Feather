import json


class StatusManager:
    def __init__(self, map_manager):
        with open("data/status/status.json") as fp:
            self.status = json.load(fp)

        self.map_manager = map_manager

    def __getitem__(self, key):
        return self.status[key]

    def __len__(self):
        return len(self.status)

    def update(self, status_dict: dict):
        for status, value in status_dict.items():
            category, status = status.split(".")
            if category == "place" and value:
                self.status["previous_place"] = self.status["place"]
                self.status["place"] = status
            else:
                self.status[category][status] = value

    def check_status(self, status: str):
        for elt in status.split(","):
            elt = elt.strip()
            if elt[0] == "!":
                category, status_name, *level = elt[1:].split(".")
                if category == "place" and self.status["place"] == status_name:
                    return False
                elif (
                    status_name in self.status[category]
                    and self.status[category][status_name]
                ):
                    return False
            else:
                category, status_name, *level = elt.split(".")
                if category == "place" and self.status["place"] != status_name:
                    if not self.map_manager.is_subplace(
                        self.status["place"], status_name
                    ):
                        return False
                elif status_name not in self.status[category]:
                    return False
                elif (
                    category not in ["place", "previous_place"]
                    and not self.status[category][status_name]
                ):
                    return False

        return True

    def is_alone(self):
        if "presence" in self.status:
            for people in self.status["presence"]:
                if self.status["presence"][people]:
                    return False

        return True

    def is_dead(self):
        if "dead" in self.status["physical_state"]:
            return True
        return False

    def get_presence(self):
        return [p for p, there in self.status["presence"].items() if there]

    def get_current_place(self):
        return self.status["place"]
