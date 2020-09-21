import json

replacements = {
    "phone": ["telephone"],
    "university": ["school", "college"],
    "spell": ["incantation"],
    "app": ["application"],
    "flashlight": ["torch"],
    "spirit": ["ghost"]
}

if __name__ == '__main__':
    repl = {}
    for word, word_list in replacements.items():
        for w in word_list:
            repl[w] = word
    
    with open("../../data/generated/replacements.json", "w") as fd:
        json.dump(repl, fd)