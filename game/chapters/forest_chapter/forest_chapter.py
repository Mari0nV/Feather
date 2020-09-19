from game.generic_mapping import generic_mapping
from game.chapters.chapter import Chapter
from game.chapters.forest_chapter.forest_mapping import forest_mapping
import random


class ForestChapter(Chapter):
    def __init__(self, game_manager):
        Chapter.__init__(self, game_manager)

    def process_response(self, response):
        self.choose_action(response, forest_mapping, generic_mapping)
