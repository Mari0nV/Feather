forest_mapping = {
    "get up": {
        ("physical_state.laying"): {
            "msg": ["You get up and remove the leafs hung up on your clothes. Man you're dirty. You better go back quicky to your dorm room to clean up."],
            "update": {"physical_state.laying": False},
            },
        (): {
            "msg": ["You are already standing up."],
            }
    },
    "sleep": {
        ("mental_state.tired", "!places.cemetery"): {
            "msg": ["You're so tired... You spot a somewhat-comfy pack of leaves and take a nap. " \
                    "When you wake up, it's still dark."],
            "update": {"mental_state.tired": False}
        },
        ("!mental_state.tired"): {
            "msg": "You're not tired enough to be able to sleep."
        },
        ("mental_state.tired", "places.cemetery"): {
            "msg": ["This cemetery is too creepy, you'll never find any sleep here."]
        }
    },
    "go to bed": {
        (): {
            "msg": "You bed is far away..."
        }
    },
    "go to university": {
        ("!active.gps"): {
            "msg": ["You wish you could, but you have no idea which direction to go."],
        },
        ("active.gps"): {
            "msg": ["You follow the indication of the GPS to go back to the university campus."],
            "update": {"places.university": True}
        },
        (): {
            "msg": ["You have no idea where it is."]
        }
    },
    "pick up phone": {
        ("active.phone"): {
            "msg": ["You already have your phone in your hands."],
        },
        (): {
            "msg": ["You retrieve your phone from your pocket. Surely it can help you in some way."],
            "update": {"active.phone": True}
        },
    },
    "use phone gps": {
        ("active.phone", "active.gps"): {
            "msg": ["Where do you want to go?"]
        },
        ("!active.phone"): {
            "msg": ["You pick up your phone and open your gps application. The signal is weak, but you manage to load a map of the surroundings." \
                    " University is an hour walk to the east. Every other direction shows only acres of forest."],
            "update": {"active.phone": True, "active.gps": True}
        },
        (): {
            "msg": ["You open your gps application. The signal is weak, but you manage to load a map of the surroundings." \
                    " University is an hour walk to the east. Every other direction shows only acres of forest."],
            "update": {"active.gps": True}
        }
    },
    "use phone light": {
        ("active.phone", "environment.dark"): {
            "msg": ["You open your phone light application. Finally, you're able to see what's in front of you! "],
            "update": {"environment.dark": False},
            "next": "see surroundings"
        },
        ("!active.phone", "environment.dark"): {
            "msg": ["You retrieve your phone from your pocket and open your flashlight application."],
            "update": {"environment.dark": False, "active.phone": True}
        },
        (): {
            "msg": ["You already have the light you need."]
        }
    },
    "see surroundings": {
        ("places.cemetery", "!environment.dark"): {
            "msg": ["Old and damaged tombs surround you. The ground looks like someone - or something - tried to dig up every inch of the cemetery. It's odd, right?"]
        },
        ("places.middle_forest", "!environment.dark"): {
            "msg": ["Trees are the only thing you can see. Their trunks are all cluttered and gigantic."]
        },
        ("environment.dark"): {
            "msg": ["It would be easier with some light."]
        }
    },
    "take random direction": {
        ("!places.cemetery"): {
            "msg": ["You walk aimlessly into the forest. You have faith in your destiny. Finally you arrive... into a cemetery. Weirdly, you feel colder than before."],
            "update": {"places.cemetery": True}
        },
        (): {
            "msg": ["You walk aimlessly into the forest, crossing trees and only trees. You feel like it's never ending. " \
                    "Finally, you recognize the borders of the university campus. Happy and relieved, you run towards your dormroom."],
            "update": {"places.university": True}
        }
    },
    "go north": {
        ("!places.cemetery", "active.gps"): {
            "msg": ["You walk a few minutes towards the north and arrive in a dark, tree-less field full of tombs." \
                    " The atmosphere seems to have changed, isn't it slightly colder than before?"],
            "update": {"places.cemetery": True}
        },
        ("!active.gps"): {
            "msg": ["How would you know where the north is ?"]
        },
        ("places.cemetery", "active.gps"): {
            "msg": ["You try to walk further north, but a 10-meter wall stand in your way."]
        },
    },
    "go south": {
        ("places.cemetery", "active.gps"): {
            "msg": ["You go back to where you woke up."],
            "update": {"places.middle_forest": True}
        },
        ("places.middle_forest", "active.gps"): {
            "msg": ["You walk south, not so eager to return home. " \
                    "Half an hour later, you arrive on the side of a turbulent river. The water flows dangerously above big rounded rocks."],
            "update": {"places.river": True}
        },
        ("places.river", "active.gps"): {
            "msg": ["You cannot go further south!"]
        },
        ("!active.gps"): {
            "msg": ["How would you know where the south is?"]
        }
    },
    "go east": {
        ("active.gps", "places.middle_forest"): {
            "next": "go to university"
        },
        ("active.gps", "places.west_forest"): {
            "msg": ["You go back where you woke up earlier."],
            "update": {"places.middle_forest": True}
        },
        ("!active.gps"): {
            "msg": ["You have no idea where the east is."]
        }
    },
    "go west": {
        ("!places.west_forest", "active.gps", "!physical_state.thirsty"): {
            "msg": ["You walk towards the west, unsure of what you'll find. " \
                    "The answer is... nothing. The forest seems to never end. Two hours later, you feel thirsty and hungry."],
            "update": {"physical_state.thirsty": True, "physical_state.hungry": True, "places.west_forest": True}
        },
        ("places.west_forest", "active.gps", "physical_state.thirsty", "!physical_state.dying"): {
            "msg": ["You're so thirsty... You continue to walk towards the west, but you feel weaker and weaker."],
            "update": {"physical_state.dying": True}
        },
        ("places.west_forest", "active.gps", "physical_state.dying"): {
            "msg": ["You're beyong exhausted. You continue to walk, hoping to find an exit from this dreadful forest. "\
                    "A few minutes later, you faint. Unfortunately, nobody finds you, and you just die unconsciously."],
            "next": "accidental death"
        },
        ("!active.gps"): {
            "msg": ["You have no idea where the east is."]
        }
    },
    "go back": {
        ("previous.middle_forest"): {
            "msg": ["You go back to where you woke up earlier."],
            "update": {"places.middle_forest": True}
        },
        ("previous.cemetery"): {
            "msg": ["You go back to the cemetery."],
            "update": {"places.cemetery": True}
        },
        ("previous.river"): {
            "msg": ["You go back to the river."],
            "update": {"places.river": True}
        },
        ("active.gps", "previous.west_forest"): {
            "msg": ["You go back to the west of the forest."],
            "update": {"places.west_forest": True}
        }

    },
    "accidental death": {
        (): {
            "msg": ["Your death ends the story. Maybe you'll do better next time!"],
            "update": {"physical_state.dead": True}
        }
    },
    "put phone in pocket": {
        ("active.phone"): {
            "msg": ["You put your phone in your pocket."],
            "update": {"active.phone": False}
        },
        (): {
            "msg": ["You phone is already in your pocket."]
        }
    },
    "climb tree": {
        ("!places.cemetery"): {
            "msg": ["You approach the closest tree and try to climb it. "\
                    "However you have no climbing skills, and you fall ridiculously on the ground."],
            "update": {"physical_state.laying": True}
        },
        ("places.cemetery"): {
            "msg": ["There is no tree inside this cemetery."]
        }
    },
    "summon spirit": {
        ("places.cemetery"): {
            "msg": ["You're in a cemetery at night... Seems like the perfect time and place to summon spirits. " \
                "You have no idea how to do it, so you mumble some random gibberish.  " \
                    "\"bjao imaaa gluglu tiiiii, sassowi maaaa...\" " \
                        "Suddenly, a spirit made of a shimmering light appears in front of you."],
            "update": {"active.spirit": True, "presence.spirit": True}
        },
        ("active.spirit"): {
            "msg": ["You already summoned a spirit. The Invisible Realm rules state that you can only have one "\
                    "eery companion at a time."]
        },
        (): {
            "msg": ["You try to summon a spirit by murmuring some gibberish words, but nothings happens. " \
                "Maybe the place isn't right? (Or you have no magical power, but can you really accept that conclusion?)"]
        }
    },
    "touch spirit": {
        ("active.spirit"): {
            "msg": ["You try to touch the spirit but your hand passes through it. You feel a cold sensation in your entire body."],
        },
        (): {
            "msg": ["What are you talking about?"]
        }
    },
    "swim in river": {
        ("!places.river"): {
            "msg": ["There is no water around you."]
        },
        ("places.river"): {
            "msg": ["You remove your clothes and approach the river. The water is cold, but the adrenaline gives you courage. " \
                    "You go in and enjoy the water flowing on your body. Unfortunately, the flow is too strong and makes you slip on a rock. " \
                    "You're torned up and die quite painfully."],
            "next": "accidental death"
        }
    }
    
}
