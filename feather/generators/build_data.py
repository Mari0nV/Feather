import itertools
import json
import re
import os

from feather.config import (
    action_path,
    dialog_combinations_file,
    generated_action_file,
    generated_dialog_combinations_file,
    generated_dialog_file,
    generated_move_combinations_file,
    generated_path,
    generated_replacements_file,
    move_combinations_file,
    replacements_file,
    speech_path
)
from feather.generators.build_map import build_map_data


def build_dictionary(source_files, dest_path):
    dictionary = {}
    for json_file in source_files:
        with open(json_file, "r") as fp:
            combinations = json.load(fp)["combinations"]
        key = json_file.split("/")[-1].split(".")[0]

        for group in combinations:
            for combination in itertools.product(*group.values()):
                word = re.sub(" +", " ", " ".join(combination))
                dictionary[word.strip()] = key

    with open(dest_path, "w+") as fd:
        json.dump(dictionary, fd)


def build_combinations(source_file, dest_file):
    all_combinations = []

    with open(source_file, "r") as fp:
        combinations = json.load(fp)["combinations"]

    for group in combinations:
        for combination in itertools.product(*group.values()):
            word = re.sub(" +", " ", " ".join(combination))
            all_combinations.append(word.strip())

    with open(dest_file, "w+") as fd:
        json.dump({"combinations": all_combinations}, fd)


def build_replacements():
    with open(replacements_file, "r") as fp:
        replacements = json.load(fp)["replacements"]

    repl = {}
    for word, word_list in replacements.items():
        for w in word_list:
            repl[w] = word

    with open(generated_replacements_file, "w+") as fd:
        json.dump(repl, fd)


def build_data():
    if not os.path.exists(generated_path):
        os.mkdir(generated_path)

    # Building speeches
    dialogs = [
        f"{speech_path}/{f}"
        for f in os.listdir(speech_path)
        if os.path.isfile(os.path.join(speech_path, f))
    ]

    build_dictionary(dialogs, generated_dialog_file)

    # Building actions
    actions = [
        f"{action_path}/{f}"
        for f in os.listdir(action_path)
        if os.path.isfile(os.path.join(action_path, f))
    ]
    build_dictionary(actions, generated_action_file)

    # Building move combinations
    build_combinations(move_combinations_file, generated_move_combinations_file)

    # Building dialog combinations
    build_combinations(dialog_combinations_file, generated_dialog_combinations_file)

    # Building replacements
    build_replacements()

    # Building map and map aliases
    build_map_data()
