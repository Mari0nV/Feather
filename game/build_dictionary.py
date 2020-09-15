import json

actions = {
    "get up": {
        "verbs": ["get up", "stand up", "stand", "rise", "get on feet"],
        "next": ["", "on my feet"],
    },
    "go to university": {
        "verbs": ["go to", "go towards", "go", "run towards", "run to", "walk to", "walk towards", "move to", "move towards", "come to", "come towards"],
        "next": ["university", "east"]
    },
    "summon spirit": {
        "verbs": ["summon", "call", "cast", "recite"],
        "next": ["spirit", "magic", "incantation", "ghost"],
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
        "verbs": ["jerk off", "masturbate"],
        "next": [""]
    },
    "irrelevant": {
        "verbs": ["scratch", "stretch"],
        "next": [""]
    },
    "pick up phone": {
        "verbs": ["pick up", "pick", "get", "take", "use", "try", "take up"],
        "next": ["phone", "mobile"]
    },
    "use phone gps": {
        "verbs": ["use", "open"],
        "next": ["phone gps", "gps", "mobile gps", "gps app", "phone gps app", "mobile gps app", "gps on phone", "internet"]
    },
    "use phone light": {
        "verbs": ["use", "open"],
        "next": ["light app", "light"]
    },
    "put phone in pocket": {
        "verbs": ["put", "put away"],
        "next": ["phone", "phone in pockets", "phone in pocket"]
    },
    "go north": {
        "verbs": ["go", "go to", "go towards", "walk to", "walk towards", "walk", "run", "run to", "run towards"],
        "next": ["north"]
    },
    "go south": {
        "verbs": ["go", "go to", "go towards", "walk to", "walk towards", "walk", "run", "run to", "run towards"],
        "next": ["south"]
    },
    "go east": {
        "verbs": ["go", "go to", "go towards", "walk to", "walk towards", "walk", "run", "run to", "run towards"],
        "next": ["east"]
    },
    "go west": {
        "verbs": ["go", "go to", "go towards", "walk to", "walk towards", "walk", "run", "run to", "run towards"],
        "next": ["west"]
    },
    "see surroundings": {
        "verbs": ["see", "watch", "inspect", "view"],
        "next": ["surroundings", "environs", "landscape", "scenery", "around", "all around", "things", "objects"]
    },
    "sleep": {
        "verbs": ["go back to sleep", "sleep", "take nap"],
        "next": [""]
    },
    "go to bed": {
        "verbs": ["go", "go to", "rest in", "lay", "lay in"],
        "next": ["bed", "bedroom", "mattress"]
    },
    "impossible": {
        "verbs": ["fly", "do telekinesis", "perform telekinesis", "teleport"],
        "next": [""]
    },
    "die": {
        "verbs": ["die", "kill yourself", "kill myself"],
        "next": [""]
    },
    "take random direction": {
        "verbs": ["take", "go", "choose", "walk", "run"],
        "next": ["random", "randomly", "random direction", "random way", "some way", "some direction", "random path", "some path", "aimlessly"]
    },
    "swim in river": {
        "verbs": ["swim", "swim in", "bathe", "bathe in", "jump", "jump in"],
        "next": ["river", "water"]
    },
    "climb tree": {
        "verbs": ["climb", "climb up", "escalate"],
        "next": ["tree"]
    }
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
