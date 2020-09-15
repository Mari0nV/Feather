import nltk
from autocorrect import Speller
import spacy
import random


class Chapter:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.speller = Speller()

    def _variant_responses(self, response):
        # TODO handle different verbs conjugaisons
        pass

    def _skin_response(self, response):
        text = nltk.word_tokenize(response)

        # replacing some words
        for i, word in enumerate(text):
            if word in self.game_manager.replacements:
                text[i] = self.game_manager.replacements[word]

        result = nltk.pos_tag(text)
        skinned = ""

        # removing superfluous
        for word, word_type in result:
            if word not in ["i", "my", "you", "your"] and word_type not in ["RB", "AT", "DET"]:
                skinned += f"{word} "

        return skinned[:-1]

    def find_mapping(self, response, *mappings):
        # check spelling
        response = self.speller(response)

        # remove subject, possessive, pronouns, adjectives
        response = self._skin_response(response.lower())

        # check if response is in dictionary
        if response in self.game_manager.dictionary:
            data = self.game_manager.dictionary[response]
            for mapping in mappings:
                if data in mapping:
                    return mapping[data], response
        else:
            # nlp_response = self.nlp(response)
            # best_sim = {
            #     "similarity": 0,
            #     "expression": None,
            #     "mapping": None
            # }
            # for mapping in mappings:
            #     for key in mapping:
            #         sim = nlp_response.similarity(self.nlp(key))
            #         if sim > best_sim["similarity"]:
            #             best_sim.update(similarity=sim, expression=key, mapping=mapping)
            # return best_sim["mapping"][best_sim["expression"]]
            return None, response

        return None, response
    
    def update_status(self, update):
        self.game_manager.status.update(update)
    
    def do_action(self, action, skinned_resp, *mappings):
        if "msg" in action:
            print('\n', random.choice(action["msg"]).format(action=skinned_resp))
        if "update" in action:
            self.update_status(action["update"])
        if "next" in action:
            self.choose_action(action["next"], *mappings)

    def choose_action(self, response, *mappings):
        options, skinned_resp = self.find_mapping(response, *mappings)
        if options:
            for status, action in options.items():
                if status:
                    status_list = [status] if type(status) == str else list(status)
                    if self.game_manager.status.check_status(status_list):
                        self.do_action(action, skinned_resp, *mappings)
                        return

            self.do_action(action, skinned_resp, *mappings)
                    


