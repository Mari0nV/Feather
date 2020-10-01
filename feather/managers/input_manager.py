from abc import ABC, abstractmethod
import json
import nltk
import random
from autocorrect import Speller

from feather.config import generated_replacements_file
from feather.utils.utils import remove_punctuation


class InputManager(ABC):
    def __init__(self, output_manager):
        with open(generated_replacements_file) as json_file:
            self.replacements = json.load(json_file)

        self.speller = Speller()
        self.output_manager = output_manager

    def _variant_responses(self, response):
        # TODO handle different verbs conjugaisons
        pass

    def _clean_response(self, response):
        # check spelling
        response = self.speller(response)

        # remove punctuation
        response = remove_punctuation(response)

        text = nltk.word_tokenize(response.lower())
        tags = nltk.pos_tag(text)

        # replacing some words
        for i, word in enumerate(text):
            if word in self.replacements:
                text[i] = self.replacements[word]
                tags[i] = (self.replacements[word], tags[i][1])

        # removing superfluous words
        clean_response = ""
        for word, word_type in tags:
            if word not in ["i", "my"] and word_type not in [
                "AT", "DET", "DT"]:
                clean_response += f"{word} "

        return clean_response[:-1]

    @abstractmethod
    def _retrieve_action(self, clean_response):
        pass

    def process_response(self, response):
        # check spelling, replace and remove some words
        clean_response = self._clean_response(response)

        # save clean response in history of inputs/outputs
        self.output_manager.save_input(clean_response)

        # retrieve action from dictionary and status checking
        action = self._retrieve_action(clean_response)

        # perform choosen action
        if action:
            self._do_action(action, clean_response)

    def _do_action(self, action, clean_resp):
        if "msg" in action:
            self.output_manager.print(
                random.choice(action["msg"]).format(action=clean_resp)
            )
        if "update" in action:
            self.status_manager.update(action["update"])
        if "next" in action:
            self.process_response(action["next"])
