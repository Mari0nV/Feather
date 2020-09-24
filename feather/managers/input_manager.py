import json

import nltk
from autocorrect import Speller
from feather.config import replacements_file


class InputManager:
    def __init__(self):
        with open(replacements_file) as json_file:
            self.replacements = json.load(json_file)

        self.speller = Speller()

    def _variant_responses(self, response):
        # TODO handle different verbs conjugaisons
        pass

    def _preprocess_response(self, response):
        # check spelling
        response = self.speller(response)

        text = nltk.word_tokenize(response.lower())
        tags = nltk.pos_tag(text)

        return text, tags
