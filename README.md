# Feather

Feather is a game where you write down any action that comes to your mind, and read their consequences on the Feather world. You can explore the world, solve intrigues and build relationships with a lot of freedom. Be aware, because you can die depending on the actions you make.

## Setup

You wake up in the middle of a forest at night, with no idea how you got here. You're a freshman at the Strangeland University, so maybe it's a prank from students.
It's up to you to decide what you do and where you go at this point.

## Usage

Clone this repository and type the following commands:
```
pip install .
build_data  # generates data json files
python game/main.py
```

A small text introduction will be displayed. Write whatever action or dialog you wish to make (one action at a time, and usually starting with a verb).
Examples:
```
go to the university
take a nap
say hello to Wendy
```

## Contribute to the story

If you wish to contribute to the story, you can create json files in the folder ```data``` with new routes.

### Action routes

You can define actions in ```data/actions/``` in the form of a json file. The name of the file must correspond to the key of the action (for example, ```climb_tree.json``` will contain information on the action "climb tree". The json file contains two dictionaries : one describing the consequences of the action depending on one or multiple status, and one describing all the combinations of words that will lead to this action.


For example, ```climb_tree.json``` could look like:
```
{
    "climb_tree": {
        "place.forest, !skills.climbing": {
            "msg": ["You approach the closest tree and try to climb it. However you have no climbing skills, and you fall ridiculously on the ground."],
            "update": {"physical_state.laying": true}
        },
        "place.forest, skills.climbing": {
            "msg": ["You approach the closest tree and climb it to the top. You can see the university not far away."],
            "update": {"information.university": true}
        },
        "!place.forest": {
            "msg": ["There is no tree here."]
        }
    },
    "combinations": [
            {
            "part1": ["climb", "scale"],
            "part2": ["on", ""],
            "part2": ["tree"]
            }
        ]
}
```
