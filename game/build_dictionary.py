import json

actions = {
    "get up": {
        "verbs": ["get up", "stand up", "stand", "rise", "get on feet"], # add 'I' option
        "next": ["", "on my feet"],
    },
    "go to university": {
        "verbs": ["go to", "go towards", "go", "run towards", "run to", "walk to", "walk towards", "move to", "move towards", "come to", "come towards"],
        "next": ["university"]
    },
    "perform incantation": {
        "verbs": ["perform", "do", "cast", "recite"],
        "next": ["spell", "magic", "incantation"],
    },
    "create wand": {
        "verbs": ["create", "build", "generate", "conceive"],
        "next": ["magic artefact", "wand", "magic wand"]
    },
    "obvious": {
        "verbs": ["breathe"],
        "next": ["", "in", "out"]
    },
    "inappropriate": {
        "verbs": ["jerk off"],
        "next": [""]
    },
    "irrelevant": {
        "verbs": ["scratch", "stretch"],
        "next": [""]
    },
}

if __name__ == '__main__':
    dictionary = {}
    for expression, components in actions.items():
        for verb in components["verbs"]:
            for next_words in components["next"]:
                if next_words:
                    response = f"{verb} {next_words}"
                else:
                    response = verb
                dictionary[response] = expression
    
    with open("../data/dictionary.json", "w") as fd:
        json.dump(dictionary, fd)
