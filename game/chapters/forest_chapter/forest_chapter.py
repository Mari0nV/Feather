from game.chapters.chapter import Chapter
from game.chapters.forest_chapter.forest_mapping import forest_mapping


class ForestChapter(Chapter):
    def __init__(self):
        Chapter.__init__(self, forest_mapping)
