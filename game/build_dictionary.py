import json
from game.chapters.action_dictionary import actions
from game.dialog.dialog_dictionary import lines



def build_dictionary(dictionary_dict, filename):
    dictionary = {}
    for expression, components in dictionary_dict.items():
        for verb in components["verbs"]:
            for next_words in components["next"]:
                if next_words:
                    response = f"{verb} {next_words}"
                else:
                    response = verb
                dictionary[response] = expression
    
    with open(f"../data/{filename}.json", "w") as fd:
        json.dump(dictionary, fd)

if __name__ == '__main__':
    build_dictionary(actions, "action_dictionary")
    build_dictionary(lines, "dialog_dictionary")
