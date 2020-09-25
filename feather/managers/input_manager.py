import json

import nltk
import random
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

    def _retrieve_action(self, skinned_response):
        pass

    def _skin_response(self, text, tags):
        # replacing some words
        for i, word in enumerate(text):
            if word in self.replacements:
                text[i] = self.replacements[word]
                tags[i] = (self.replacements[word], tags[i][1])

        skinned = ""
        # removing superfluous
        for word, word_type in tags:
            if word not in ["i", "my", "you", "your"] and word_type not in [
                "AT",
                "DET",
            ]:
                skinned += f"{word} "

        return skinned[:-1]

    def process_response(self, response):
        # check spelling and decompose response
        text, tags = self._preprocess_response(response)

        # remove subject, possessive, pronouns...
        skinned_response = self._skin_response(text, tags)

        # retrieve action from dictionary and status checking
        action = self._retrieve_action(skinned_response)

        # perform choosen action
        if action:
            self._do_action(action, skinned_response)

    def _do_action(self, action, skinned_resp):
        if "msg" in action:
            self.output_manager.print(
                random.choice(action["msg"]).format(action=skinned_resp)
            )
        if "update" in action:
            self.status_manager.update(action["update"])
        if "next" in action:
            self.process_response(action["next"])
