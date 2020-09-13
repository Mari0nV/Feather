import nltk
from autocorrect import Speller


class Chapter:
    def __init__(self, game_manager):
        self.dictionary = game_manager.dictionary
        self.speller = Speller()
    
    def _variant_responses(self, response):
        # TODO handle different verbs conjugaisons
        pass

    def _skin_response(self, response):
        text = nltk.word_tokenize(response)
        result = nltk.pos_tag(text)
        skinned = ""

        # removing superfluous
        for word, word_type in result:
            if word not in ["i", "my", "you", "your"] and word_type not in ["RB", "JJ", "AT", "DET"]:
                skinned += f"{word} "

        return skinned[:-1]

    def find_mapping(self, response, *mappings):
        # check spelling
        response = self.speller(response)

        # remove subject, possessive, pronouns, adjectives
        response = self._skin_response(response.lower())

        # check if response is in dictionary
        if response in self.dictionary:
            data = self.dictionary[response]
            for mapping in mappings:
                if data in mapping:
                    return mapping[data]

        return None
