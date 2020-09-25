import itertools
import json
import re
import os

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def build_dictionary(json_files, filename):
    dictionary = {}
    for json_file in json_files:
        with open(json_file, "r") as fp:
            combinations = json.load(fp)["combinations"]
        key = json_file.split("/")[-1].split(".")[0]

        for group in combinations:
            for combination in itertools.product(*group.values()):
                word = re.sub(" +", " ", " ".join(combination))
                dictionary[word.strip()] = key

    with open(f"data/generated/{filename}.json", "w+") as fd:
        json.dump(dictionary, fd)


def build_combinations(json_file, filename):
    all_combinations = []

    with open(json_file, "r") as fp:
        combinations = json.load(fp)["combinations"]

    for group in combinations:
        for combination in itertools.product(*group.values()):
            word = re.sub(" +", " ", " ".join(combination))
            all_combinations.append(word)

    with open(f"data/generated/{filename}.json", "w+") as fd:
        json.dump({"combinations": all_combinations}, fd)


def build_replacements(json_file, filename):
    with open(f"data/{filename}.json", "r") as fp:
        replacements = json.load(fp)["replacements"]

    repl = {}
    for word, word_list in replacements.items():
        for w in word_list:
            repl[w] = word

    with open(f"data/generated/{filename}.json", "w+") as fd:
        json.dump(repl, fd)


if __name__ == "__main__":
    if not os.path.exists("data/generated"):
         os.mkdir("data/generated")

    # Building speech dictionary
    dialog_path = "data/dialog/speech"
    dialog_path = "data/dialog"
    dialogs = [
        f"{dialog_path}/{f}"
        for f in os.listdir(dialog_path)
        if os.path.isfile(os.path.join(dialog_path, f))
    ]

    build_dictionary(dialogs, "speech_dictionary")

    # Building dialog combinations
    dialog_combinations_path = "data/dialog/combinations.json"
    build_combinations(dialog_combinations_path, "dialog_combinations")

    # Building action dictionary
    action_path = "data/action"
    actions = [
        f"{action_path}/{f}"
        for f in os.listdir(action_path)
        if os.path.isfile(os.path.join(action_path, f))
    ]
    build_dictionary(actions, "action_dictionary")

    # Building move combinations
    move_path = "data/move/combinations.json"
    build_combinations(move_path, "move_combinations")

    # Building replacements dictionary
    replacement_path = "data/replacements.json"
    build_replacements(replacement_path, "replacements")
