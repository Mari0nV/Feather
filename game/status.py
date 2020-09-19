import json


class Status:
    def __init__(self):
        with open('../data/status.json') as json_file:
            self.status = json.load(json_file)
    
    def __getitem__(self, key):
        return self.status[key]
    
    def __len__(self):
        return len(self.status)
    
    def update(self, status_dict: dict):
        for status, value in status_dict.items():
            category, status = status.split('.')
            if category == "places":
                for place in self.status[category]:
                    if self.status[category][place] == True:
                        self.status["previous"] = {
                            place: True
                        }
                        self.status[category][place] = False
                

            self.status[category][status] = value
    
    def check_status(self, status: list):
        for elt in status:
            if elt[0] == '!':
                category, status_name, *level = elt[1:].split('.')
                if status_name in self.status[category] and self.status[category][status_name]:
                    return False
            else:
                category, status_name = elt.split('.')
                if status_name not in self.status[category] or not self.status[category][status_name]:
                    return False

        return True
    
    def is_alone(self):
        if "presence" in self.status:
            for people in self.status["presence"]:
                if self.status["presence"][people] == True:
                    return False
        
        return True
