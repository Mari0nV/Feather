import json


class Status:
    def __init__(self):
        with open('../data/status.json') as json_file:
            self.states = json.load(json_file)
    
    def update(self, status_dict: dict):
        for status, value in status_dict.items():
            category, status = status.split('.')
            self.states[category][status] = value
    
    def check_status(self, status: list):
        for elt in status:
            if elt[0] == '!':
                category, status_name = elt[1:].split('.')
                if status_name in self.states[category] and self.states[category][status_name]:
                    return False
            else:
                category, status_name = elt.split('.')
                if status_name not in self.states[category] or not self.states[category][status_name]:
                    return False

        return True
