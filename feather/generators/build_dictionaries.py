import itertools
import json
import re
from os import listdir
from os.path import isfile, join


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


def build_replacements(json_file, filename):
    with open(f"data/{filename}.json", "r") as fp:
        replacements = json.load(fp)["replacements"]

    repl = {}
    for word, word_list in replacements.items():
        for w in word_list:
            repl[w] = word

    with open("data/generated/{filename}.json", "w") as fd:
        json.dump(repl, fd)


if __name__ == "__main__":
    dialog_path = "data/dialog"
    dialogs = [
        f"{dialog_path}/{f}"
        for f in listdir(dialog_path)
        if isfile(join(dialog_path, f))
    ]

    build_dictionary(dialogs, "dialog_dictionary")

    action_path = "data/action"
    actions = [
        f"{action_path}/{f}"
        for f in listdir(action_path)
        if isfile(join(action_path, f))
    ]
    build_dictionary(actions, "action_dictionary")

    move_path = "data/move/combinations.json"
    build_dictionary([move_path], "move_dictionary")

    replacement_path = "data/replacements.json"
    build_replacements(replacement_path, "replacements")
