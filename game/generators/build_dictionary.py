import json
from os import listdir
from os.path import isfile, join
import itertools
import re


def build_dictionary(json_files, filename):
    dictionary = {}
    for json_file in json_files:
        print(json_file)
        with open(json_file, "r") as fp:
            combinations = json.load(fp)["combinations"]
        key = json_file.split('/')[-1].split('.')[0]
        
        for group in combinations:
            for combination in itertools.product(*group.values()):
                word = re.sub(' +', ' ', " ".join(combination))
                dictionary[word.strip()] = key

    with open(f"../../data/generated/{filename}.json", "w+") as fd:
        json.dump(dictionary, fd)


if __name__ == '__main__':
    dialog_path = "../../data/dialog"
    dialogs = [f"{dialog_path}/{f}" for f in listdir(dialog_path) if isfile(join(dialog_path, f))]

    build_dictionary(dialogs, "dialog_dictionary")


    action_path = "../../data/action"
    actions = [f"{action_path}/{f}" for f in listdir(action_path) if isfile(join(action_path, f))]
    build_dictionary(actions, "action_dictionary")
    
