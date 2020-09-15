import json

replacements = {
    "phone": ["mobile", "telephone"],
    "university": ["school", "college"],
    "spell": ["incantation"],
    "app": ["application"],
    "light": ["flashlight", "torch"]
}

if __name__ == '__main__':
    repl = {}
    for word, word_list in replacements.items():
        for w in word_list:
            repl[w] = word
    
    with open("../data/replacements.json", "w") as fd:
        json.dump(repl, fd)