from game.generic_mapping import generic_mapping
from game.chapter import Chapter
from game.forest_chapter.mapping import mapping
import random


class ForestChapter(Chapter):
    def __init__(self, game_manager):
        self.all_status = game_manager.all_status
        Chapter.__init__(self, game_manager)

    def choose_action(self, response):
        choices = self.find_mapping(response, mapping, generic_mapping)

        if choices:
            for status_tuple, action in choices.items():
                if type(status_tuple) == str:
                    list_status = [self.all_status[status_tuple]]
                else:
                    list_status = [self.all_status[status] for status in status_tuple]
                    if all(list_status) or status_tuple == "finally":
                        print(random.choice(action["msg"]).format(action=response))
                        break

    def process_response(self, response):
        self.choose_action(response)
